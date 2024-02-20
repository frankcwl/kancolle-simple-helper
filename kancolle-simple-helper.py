from PyQt5.QtWidgets import QApplication
import threading
import pyautogui
import pyscreeze

pyautogui.FAILSAFE = False
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

from util.logger import logger
from gui.gui import GUI
from module.sortie import Sortie

class Kancolle(GUI):
    def __init__(self):
        super().__init__()
        self.running = False
    
    def enable_pressed(self):
        logger.debug(f'{self.map_names.currentIndex() = }')
        if self.map_names.currentIndex() == -1:
            return
        super().enable_pressed()
        self.running = not self.running
        if self.running:
            logger.info('running ' + self.map_names.currentText())
            self.run_flag = threading.Event()
            self.run_flag.set()
            sortie = Sortie(self.map_names.currentText(), self.run_flag)
            self.run = threading.Thread(target=sortie.run, args=[self.set_formation])
            self.run.daemon = True
            self.run.start()
        else:
            logger.info('stop ' + self.map_names.currentText())
            self.run_flag.clear()

if __name__ == '__main__':
    app = QApplication([])
    kancolle = Kancolle()
    kancolle.show()
    app.exec_()