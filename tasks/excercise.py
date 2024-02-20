from tasks.combat import fight_once
from util.util import *
from tasks.supply import supply

def manoeuvres_once():
    s_lst = search_all('victory_s')
    a_lst = search_all('victory_a')
    b_lst = search_all('victory_b')
    c_lst = search_all('defeat_c')
    d_lst = search_all('defeat_d')
    result_lst = []
    result_lst.extend(s_lst)
    result_lst.extend(a_lst)
    result_lst.extend(b_lst)
    result_lst.extend(c_lst)
    result_lst.extend(d_lst)
    flag_lst = search_all('flag')
    valid_flag = None
    for flag in flag_lst:
        for result in result_lst:
            if abs(flag.top - result.top) < 20:
                break
        else:
            valid_flag = flag
            break
    if not valid_flag:
        logger.info('manoeuvres over')
        return None
    click(valid_flag)
    click_until_true('manoeuvres_choose')
    click_until_true('manoeuvres_start')
    fight_once(night_battle=True,attack=None)
    return valid_flag
    
def manoeuvres():
    while True:
        click_until_true('fight')
        click_until_true('manoeuvres')
        check_until_true('flag')
        status =  manoeuvres_once()
        if status is None:
            click_until_true('home')
            break
        else:
            supply()
            move_reset()

if __name__ == '__main__':
    manoeuvres()