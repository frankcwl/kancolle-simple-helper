from util.util import *
from threading import Event
from util.logger import logger

from module.sea_map import SeaMap

from buttons.assets_battle import *
from buttons.assets_page import MAIN_PAGE
from buttons.assets_map import *
from buttons.assets_sortie import *

class Sortie():
    def __init__(self, map_name: str, run_flag: Event):
        self.run_flag = run_flag
        self.map_name = map_name
        self.map = SeaMap.get_map_by_name(map_name)
        self.nodes = self.map.nodes
        self.battle_num = len(self.nodes)
    
    def go_to_map(self):
        logger.info('go to map ' + self.map_name)
        sea_num = self.map_name[0]
        map_num = self.map_name[2]
        smooth_sleep(10, self.run_flag, random=True)
        click_until_true(SORTIE, wait=1)
        click_until_true(SORTIE2, wait=1)
        click_until_true(MAP7, wait=1)
        click_until_true(MAP_EO, wait=1)
        click_until_true(MAP7_5, wait=1)
        click_until_true(DECIDE, wait=1)
        click_until_true(FIGHT_START, wait=8)
        logger.info('sortie ' + self.map_name)
        
        
    def run(self, set_formation, run_count=-1):
        n = 0
        nodes = self.nodes
        next_formation = nodes[0].formation
        night = nodes[0].night
        retreat = nodes[0].retreat
        set_formation(next_formation, night)
        count = 0
        big_damage = False
        while self.run_flag.is_set() and count != run_count:
            # 检测到主页
            if check(MAIN_PAGE, confidence=0.9):
                logger.info('checked MAIN_PAGE')
                n = 0
                next_formation = nodes[0].formation
                set_formation(next_formation, nodes[0].night)
                if '循环' in self.map_name:
                    self.go_to_map()
            # 基地航空队
            if n == 0 and check(LBAS_ATTACK):
                logger.info('checked LBAS_ATTACK')
                while not click(LBAS_COMPLETE, wait=0.5):
                    click(self.map.LBAS, wait= 0.3)
            # 检测阵型选择
            if next_formation and check(next_formation.button):
                sleep(0.2)
                click(next_formation.button)
                count += 1
                night = nodes[n].night
                retreat = nodes[n].retreat
                n = n + 1
                if n >= self.battle_num:
                    n = 0
                next_formation = nodes[n].formation
                set_formation(next_formation, night)
                smooth_sleep(30, self.run_flag)
            # 可选分歧点
            if nodes[n].side and check(SIDE_ROAD):
                click(nodes[n].side)
            # 是否夜战
            if night:
                click(NIGHT_BATTLE, confidence=0.8)
            else:
                click(NO_FIGHT, confidence=0.8)
            # 是否撤退
            if retreat or big_damage:
                click(RETREAT, confidence=0.8)
            else:
                click(ATTACK)
            click(NEXT, confidence=0.6)
            click(COMPASS)
            click(BACK)
            if check(BIG_DAMAGE, confidence=0.8):
                big_damage = True
        set_formation()
        
if __name__ == '__main__':
    def test(*args, **kwargs):
        logger.debug(args, kwargs)
    
    SeaMap.load_map()
    flag = Event()
    flag.set()
    sortie = Sortie('7-1', flag)
    sortie.run(test)