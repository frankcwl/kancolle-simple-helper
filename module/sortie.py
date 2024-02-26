from util.util import *
from threading import Event
from util.logger import logger

from module.sea_map import SeaMap

from buttons.assets_battle import *
from buttons.assets_page import MAIN_PAGE

class Sortie():
    def __init__(self, map_name: str, run_flag: Event):
        self.run_flag = run_flag
        self.nodes = SeaMap.get_nodes(map_name)
        self.battle_num = len(self.nodes)
        
    def run(self, set_formation, run_count=-1):
        n = 0
        nodes = self.nodes
        next_formation = nodes[0].formation
        night = nodes[0].night
        retreat = nodes[0].retreat
        set_formation(next_formation, night)
        count = 0
        while self.run_flag.is_set() and count != run_count:
            # 检测到主页
            if n != 0 and check(MAIN_PAGE, confidence=0.9):
                logger.info('checked MAIN_PAGE')
                n = 0
                next_formation = nodes[0].formation
                set_formation(next_formation, nodes[0].night)
            # 检测阵型选择
            if next_formation and click(next_formation.button):
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
            if retreat:
                click(RETREAT, confidence=0.8)
            else:
                click(ATTACK)
            click(NEXT, confidence=0.7)
            click(COMPASS)
            click(BACK)
            count += 1
        set_formation()
        
if __name__ == '__main__':
    def test(*args, **kwargs):
        logger.debug(args, kwargs)
    
    SeaMap.load_map()
    flag = Event()
    flag.set()
    sortie = Sortie('7-1', flag)
    sortie.run(test)