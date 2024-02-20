from util.util import *

def expedition_check():
    expedition_name = None
    fleet_name = None
    # 检查远征名
    for num in ['02','06']:
        if check('expedition' + num + '_name'):
            expedition_name = 'expedition' + num
            break
    # 检查舰队名
    for num in ['3','4']:
        if check('fleet' + num + '_name'):
            fleet_name = 'fleet' + num
            break
    if not expedition_name or not fleet_name:
        return None
    else:
        return expedition_name, fleet_name

# 远征
def expedition():
    expedition_info = []
    # 有归还消息时
    while check('expedition_complete') is not None:
        logger.info('expedtion checked')
        click_anywhere(wait=5)
        click_until_true('next', interval=1, wait=0.5)
        
        # 储存远征信息
        info = expedition_check()
        logger.info(info)
        if info:
            expedition_info.append(info)
        click_until_true('next', wait=0.5)
    logger.info('expedition over')
    if not expedition_info:
        return
    # 根据信息重新发出远征
    click_until_true('fight')
    click_until_true('expedition',wait=1)
    for info in expedition_info:
        # 选择远征、决定、选择舰队、补给、远征开始
        click_until_true(info[0])
        click_until_true('decide', wait=0.5)
        click_until_true(info[1])
        click_until_true('supply1', wait=4)
        click_until_true('expedition_start', wait=3)
    click_until_true('home')
    move_reset()
    
if __name__ =='__main__':
    expedition()