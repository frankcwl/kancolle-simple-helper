from tasks.supply import supply
from util.util import *
from buttons.assets_sortie import *

class BigDamageWarning(Exception):
    pass

def move_to_map(map_name:str):
    click_until_true(SORTIE, wait=0.5)
    click_until_true(SORTIE2, wait=1)
    big_name, small_name = map_name.split('-')
    if big_name != '1':
        pass
    if small_name > '4':
        pass
    click_until_true(MAP1_1, wait=0.5)
    click_until_true(DECIDE, wait=0.5)
    click_until_true(FIGHT_START, wait=5)

def fight_once(wait=40, night_battle=False, attack=True):
    click_until_true('danzong',wait=wait)
    while not check('next', confidence=0.9) and not check('night_battle'):
        sleep(10)
    if check('night_battle'):
        if night_battle:
            click('night_battle')
        else:
            click('no_fight')
    click_until_true('next', confidence=0.9, interval=10)
    click_until_true('next', confidence=0.9)
    if attack is None:
        return
    if attack:
        click_until_true('attack', wait=5)
    else:
        click_until_true('retreat')

def fight(map_name:str):
    click_until_true('fight')
    click_until_true('fight2')
    move_to_map(map_name)
    if map_name == 'devmat':
        check_until_true('single_corps')
        fight_once()
        if check('way_BC',confidence=0.9):
            click_anywhere(wait=10)
            check_until_true('compass')
            click('refresh')
            click('reload')
        else:
            click('refresh')
            click('reload')
        click_until_true('GameStart')

if __name__ == '__main__':
    move_to_map('1-1')