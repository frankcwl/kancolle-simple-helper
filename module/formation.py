from enum import Enum
from buttons.assets_formations import *

class Formation(Enum):
    LINE_AHEAD = LINE_AHEAD
    DOUBLE_AHEAD = DOUBLE_AHEAD
    DIAMOND = DIAMOND
    ECHELON = ECHELON
    LINE_ABREAST = LINE_ABREAST
    VANGUARD = VANGUARD
    
    def __init__(self, button):
        self.button = button
    
    @staticmethod
    def name2formation(name: str):
        if name == '单纵阵':
            formation = Formation.LINE_AHEAD
        elif name == '复纵阵':
            formation = Formation.DOUBLE_AHEAD
        elif name == '轮形阵':
            formation = Formation.DIAMOND
        elif name == '梯形阵':
            formation = Formation.ECHELON
        elif name == '单横阵':
            formation = Formation.LINE_ABREAST
        elif name == '警戒阵':
            formation = Formation.VANGUARD
        else:
            raise ValueError('Invalid formation name: ' + name)
        return formation
    
    def __str__(self):
        if self == Formation.LINE_AHEAD:
            return '单纵阵'
        elif self == Formation.DOUBLE_AHEAD:
            return '复纵阵'
        elif self == Formation.DIAMOND:
            return '轮形阵'
        elif self == Formation.ECHELON:
            return '梯形阵'
        elif self == Formation.LINE_ABREAST:
            return '单横阵'
        elif self == Formation.VANGUARD:
            return '警戒阵'
        else:
            raise ValueError('Invalid formation: ' + str(self))