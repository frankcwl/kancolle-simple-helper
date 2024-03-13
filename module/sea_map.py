import json
import shutil
import os
import copy
from typing import Optional
from util.logger import logger

from module.formation import Formation

class Node():
    def __init__(self, formation: str, night: bool, side: Optional[list[int]] = None, retreat: Optional[bool] = None):
        self.formation = Formation.name2formation(formation)
        self.night = night
        self.side = side
        self.retreat = retreat
    
    def to_dict(self) -> dict[str, str | list[int] | bool]:
        node = {key: value for key, value in self.__dict__.items() if value is not None}
        node['formation'] = str(node['formation'])
        return node
        
class SeaMap():
    map_list: list['SeaMap'] = []
    
    def __init__(self, name: str, nodes: list[Node], LBAS: Optional[list[list]] = None) -> None:
        self.name = name
        self.LBAS = LBAS
        self.nodes = nodes
    
    def to_dict(self):
        sea_map = {key: value for key, value in self.__dict__.items() if value is not None}
        sea_map['nodes'] = [node.to_dict() for node in sea_map['nodes']]
        return sea_map
    
    def copy(self):
        return copy.deepcopy(self)
    
    @classmethod
    def save_map(cls) -> None:
        logger.info('saving map.json')
        with open('map.json', 'w', encoding='utf-8') as file:
            maps = []
            for sea_map in cls.map_list:
                maps.append(sea_map.to_dict())
            json.dump(maps, file, ensure_ascii=False, indent=4)
        cls.load_map()
    
    @classmethod
    def load_map(cls) -> None:
        logger.info('reading map.json')
        cls.map_list.clear()
        maps = cls._load_json()
        for map in maps:
            nodes = []
            for node in map['nodes']:
                nodes.append(Node(node['formation'], node['night'], node.get('side'), node.get('retreat')))
            cls.map_list.append(SeaMap(map['name'], nodes, map.get('LBAS')))
    
    @classmethod
    def _load_json(cls):
        # 检查是否存在有效的map.json文件
        if os.path.exists('map.json'):
            try:
                with open('map.json', 'r', encoding='utf-8') as file:
                    maps = json.load(file)
                return maps
            except json.JSONDecodeError:
                logger.error("'map.json' is not a valid JSON file.")
        else:
            logger.warning("'map.json' not found.")

        # 尝试从map.example.json复制文件
        if os.path.exists('map.example.json'):
            try:
                shutil.copy('map.example.json', 'map.json')
                with open('map.json', 'r', encoding='utf-8') as file:
                    maps = json.load(file)
                logger.info("copying from 'map.example.json'.")
                return maps
            except (json.JSONDecodeError, shutil.Error):
                logger.error("'map.example.json' is not a valid JSON file.")

        # 创建一个空白的json文件
        with open('map.json', 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        return []
            
    @classmethod
    def get_map_names(cls) -> list[str]:
        return [sea_map.name for sea_map in cls.map_list]
    
    @classmethod
    def get_map_by_name(cls, map_name: str) -> 'SeaMap':
        return next(sea_map for sea_map in cls.map_list if sea_map.name == map_name)
    
    @classmethod
    def get_map_by_num(cls, map_num: int) -> 'SeaMap':
        return cls.map_list[map_num]
    
    @classmethod
    def set_map(cls, map_num: int, sea_map: 'SeaMap') -> None:
        cls.map_list[map_num] = sea_map
    
    @classmethod
    def add_map(cls, map_num: int, sea_map: 'SeaMap') -> None:
        cls.map_list.insert(map_num, sea_map)
    
    @classmethod
    def delete(cls, map_num: int) -> None:
        cls.map_list.pop(map_num)
    
    @classmethod
    def move_up(cls, map_num: int) -> None:
        if map_num > 0:
            cls.map_list[map_num], cls.map_list[map_num - 1] = cls.map_list[map_num - 1], cls.map_list[map_num]

    @classmethod
    def move_down(cls, map_num: int) -> None:
        if map_num < len(cls.map_list) - 1:
            cls.map_list[map_num], cls.map_list[map_num + 1] = cls.map_list[map_num + 1], cls.map_list[map_num]