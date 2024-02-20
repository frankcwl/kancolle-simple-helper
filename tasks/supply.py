from util.util import *
from buttons.assets_page import HOME
from buttons.assets_supply import *

def supply(fleet_name=1):
    click_until_true(SUPPLY)
    while True:
        if check(SUPPLY_DONE):
            break
        click(SUPPLY_ALL,wait=2)
    click_until_true(HOME)
    
if __name__ == '__main__':
    supply()