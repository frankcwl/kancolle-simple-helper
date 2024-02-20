from time import sleep
import pyautogui
from util.logger import logger
from pynput.mouse import Listener
from threading import Event

def check(button, confidence=0.99, wait=0, region=(10, 113, 1210, 833)):
    if isinstance(button, str):
        # logger.debug(f'checking file: {button}')
        center = pyautogui.locateCenterOnScreen(button, confidence=confidence, region=region)
    if isinstance(button, list):
        # logger.debug(f'checking point: {button}')
        center = pyautogui.position(*button)
    if center is not None:
        logger.info(f'checked: {center} {button}')
        sleep(wait)
    return center

def click(button, confidence=0.99, wait=0, region=(10, 113, 1210, 833)):
    center = check(button, confidence=confidence, region=region)
    if center is not None:
        x,y = pyautogui.position()
        logger.info(f'click: {center} {button}')
        pyautogui.click(center)
        pyautogui.moveTo(x,y)
        sleep(wait)
    return center

def check_until_true(button, confidence=0.99, interval=0.5, wait=0):
    logger.info(f'checking file: {button}')
    while True:
        center = check(button, confidence=confidence)
        if center is not None:
            break
        else:
            sleep(interval)
    sleep(wait)
    return center

def click_until_true(button, confidence=0.99, interval=0.5, wait=0.2):
    while True:
        center = click(button, confidence=confidence, wait=0)
        if center is not None:
            break
        else:
            sleep(interval)
    sleep(wait)
    return center

def click_anywhere(wait=0.2):
    pyautogui.click(500, 500)
    sleep(wait)
    
def move_reset():
    pyautogui.moveTo(10, 10)

def search_all(button, confidence=0.9):
    path = 'pics/' + button + '.png'
    while True:
        logger.info(f'checking file: {button}.png')
        center = pyautogui.locateAllOnScreen(path, confidence=confidence)
        if center is not None:
            break
        else:
            sleep(0.5)
    return list(center)

def get_position(delay = 0) -> list[list]:
    sleep(delay)
    coordinates = []

    def on_click(x, y, button, pressed):
        if pressed:
            coordinates.append([x, y])
            listener.stop()  # 停止监听

    with Listener(on_click=on_click) as listener:
        listener.join()

    return coordinates[0]

def smooth_sleep(seconds: float, run_flag: Event):
    for _ in range(int(seconds * 10)):
        if not run_flag.is_set():
            break
        sleep(0.1 / 1.08)