from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QIcon

from gui.ui_generated import Ui_MainWindow
from gui.maps_generated import Ui_Dialog as Maps_Dialog
from gui.nodes_generated import Ui_Dialog as Nodes_Dialog
from module.sea_map import SeaMap, Node
from module.formation import Formation
from util.util import get_position

class ShowNodes(Nodes_Dialog, QDialog):
    def __init__(self, sea_map: SeaMap):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('toolkit/icon.ico'))
        self.sea_map = sea_map
        
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint | Qt.WindowStaysOnTopHint)
        
        self.map_name.setText(self.sea_map.name)
        
        self.nodes.currentItemChanged.connect(self.node_changed)
        self.refresh()
        
        self.connect_all()
        self.nodes.setCurrentRow(0)
    
    def connect_all(self):
        self.formations.currentIndexChanged.connect(self.formation_changed)
        self.night.stateChanged.connect(self.night_changed)
        self.retreat.stateChanged.connect(self.retreat_changed)
        self.map_name.textChanged.connect(self.map_name_changed)
        
        self.create_.clicked.connect(self.create_clicked)
        self.delete_.clicked.connect(self.delete_clicked)
        
        self.side_x.valueChanged.connect(self.side_changed)
        self.side_y.valueChanged.connect(self.side_changed)
        self.set_side.clicked.connect(self.set_side_clicked)
    
    def disconnect_all(self):
        self.formations.currentIndexChanged.disconnect(self.formation_changed)
        self.night.stateChanged.disconnect(self.night_changed)
        self.retreat.stateChanged.disconnect(self.retreat_changed)
        self.map_name.textChanged.disconnect(self.map_name_changed)
        
        self.create_.clicked.disconnect(self.create_clicked)
        self.delete_.clicked.disconnect(self.delete_clicked)
        
        self.side_x.valueChanged.disconnect(self.side_changed)
        self.side_y.valueChanged.disconnect(self.side_changed)
        self.set_side.clicked.disconnect(self.set_side_clicked)
    
    def node_changed(self):
        if self.nodes.currentRow() >= len(self.sea_map.nodes) or len(self.sea_map.nodes) == 0:
            return
        self.disconnect_all()
        self.node = self.sea_map.nodes[self.nodes.currentRow()]
        self.formations.setCurrentText(str(self.node.formation))
        if self.node.night:
            self.night.setChecked(True)
        else:
            self.night.setChecked(False)
        if self.node.retreat:
            self.retreat.setChecked(True)
        else:
            self.retreat.setChecked(False)
        if self.node.side:
            self.side_x.setValue(self.node.side[0])
            self.side_y.setValue(self.node.side[1])
        else:
            self.side_x.setValue(0)
            self.side_y.setValue(0)
        self.connect_all()
    
    def formation_changed(self):
        self.node.formation = Formation.name2formation(self.formations.currentText())
        node_num = self.nodes.currentRow()
        self.refresh()
        self.nodes.setCurrentRow(node_num)
    
    def night_changed(self):
        if self.night.isChecked():
            self.node.night = True
        else:
            self.node.night = False
    
    def retreat_changed(self):
        if self.retreat.isChecked():
            self.node.retreat = True
        else:
            self.node.retreat = None
    
    def map_name_changed(self):
        self.sea_map.name = self.map_name.text()
    
    def create_clicked(self):
        self.sea_map.nodes.append(Node('单纵阵', False))
        self.nodes.addItem(str(self.sea_map.nodes[-1].formation))
        self.nodes.setCurrentRow(self.nodes.count() - 1)
    
    def delete_clicked(self):
        node_num = self.nodes.currentRow()
        self.sea_map.nodes.pop(node_num)
        self.nodes.takeItem(node_num)
        self.node_changed()
    
    def side_changed(self):
        if self.side_x.value() or self.side_y.value():
            self.node.side = [self.side_x.value(), self.side_y.value()]
        else:
            self.node.side = None
    
    def set_side_clicked(self):
        self.set_side.setText('选取中')
        side = get_position()
        self.side_x.setValue(side[0])
        self.side_y.setValue(side[1])
        self.set_side.setText('选取')
    
    def refresh(self):
        self.nodes.currentItemChanged.disconnect()
        self.nodes.clear()
        self.nodes.addItems([str(node.formation) for node in self.sea_map.nodes])
        self.nodes.currentItemChanged.connect(self.node_changed)

class ShowMaps(Maps_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('toolkit/icon.ico'))
        
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint | Qt.WindowStaysOnTopHint)
        
        self.create_.clicked.connect(self.create_clicked)
        self.edit.clicked.connect(self.edit_clicked)
        self.delete_.clicked.connect(self.delete_clicked)
        
        self.move_up.clicked.connect(self.move_up_clicked)
        self.move_down.clicked.connect(self.move_down_clicked)
    
    def retranslateUi(self, Dialog):
        super().retranslateUi(Dialog)
        self.refresh()
    
    def create_clicked(self):
        map_num = self.map_names.currentRow()
        sea_map = SeaMap('new', [])
        dialog = ShowNodes(sea_map)
        ret = dialog.exec_()
        if ret == QDialog.Accepted:
            SeaMap.add_map(map_num + 1, sea_map)
            self.refresh()
            self.map_names.setCurrentRow(map_num + 1)
    
    def edit_clicked(self):
        map_num = self.map_names.currentRow()
        sea_map = SeaMap.get_map(map_num).copy()
        dialog = ShowNodes(sea_map)
        ret = dialog.exec_()
        if ret == QDialog.Accepted:
            SeaMap.set_map(map_num, sea_map)
            self.refresh()
            self.map_names.setCurrentRow(map_num)
    
    def delete_clicked(self):
        SeaMap.delete(self.map_names.currentRow())
        self.map_names.takeItem(self.map_names.currentRow())
    
    def move_up_clicked(self):
        if self.map_names.currentRow() > 0:
            map_num = self.map_names.currentRow()
            SeaMap.move_up(map_num)
            self.refresh()
            self.map_names.setCurrentRow(map_num - 1)
        
    def move_down_clicked(self):
        if self.map_names.currentRow() < self.map_names.count() - 1:
            map_num = self.map_names.currentRow()
            SeaMap.move_down(map_num)
            self.refresh()
            self.map_names.setCurrentRow(map_num + 1)
    
    def refresh(self):
        self.map_names.clear()
        for map_name in SeaMap.get_map_names():
            self.map_names.addItem(QCoreApplication.translate("Dialog", map_name))

class GUI(Ui_MainWindow, QMainWindow):
    def __init__(self):
        SeaMap.load_map()
        
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('toolkit/icon.ico'))
        self.move(1426,842)
        
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint & ~Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint)

        self.enable.pressed.connect(self.enable_pressed)
        self.reload.pressed.connect(self.reload_pressed)
    
    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        for map_name in SeaMap.get_map_names():
            self.map_names.addItem(QCoreApplication.translate("MainWindow", map_name))
    
    def set_formation(self, formation = None, night = False):
        if formation:
            self.formation_label.setText(str(formation))
        else:
            self.formation_label.setText('')
        if night:
            palette = self.formation_label.palette()
            palette.setColor(self.formation_label.foregroundRole(), Qt.red)
            self.formation_label.setPalette(palette)
        else:
            palette = self.formation_label.palette()
            palette.setColor(self.formation_label.foregroundRole(), Qt.black)
            self.formation_label.setPalette(palette)
            
    def enable_pressed(self):
        if self.enable.text() == '开启':
            self.enable.setText('停止')
            self.map_names.setEnabled(False)
            self.reload.setEnabled(False)
        else:
            self.enable.setText('开启')
            self.map_names.setEnabled(True)
            self.reload.setEnabled(True)
    
    def reload_pressed(self):
        dialog = ShowMaps()
        ret = dialog.exec_()
        if ret == QDialog.Accepted:
            SeaMap.save_map()
            current_map = self.map_names.currentText()
            self.map_names.clear()
            for map_name in SeaMap.get_map_names():
                self.map_names.addItem(QCoreApplication.translate("MainWindow", map_name))
            self.map_names.setCurrentText(current_map)
        else:
            SeaMap.load_map()