# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/nodes.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(362, 438)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.map_name = QtWidgets.QLineEdit(Dialog)
        self.map_name.setObjectName("map_name")
        self.horizontalLayout.addWidget(self.map_name)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.LBAS_label = QtWidgets.QLabel(Dialog)
        self.LBAS_label.setObjectName("LBAS_label")
        self.horizontalLayout_5.addWidget(self.LBAS_label)
        self.LBAS_x = QtWidgets.QSpinBox(Dialog)
        self.LBAS_x.setMaximum(1919)
        self.LBAS_x.setObjectName("LBAS_x")
        self.horizontalLayout_5.addWidget(self.LBAS_x)
        self.LBAS_y = QtWidgets.QSpinBox(Dialog)
        self.LBAS_y.setMaximum(1079)
        self.LBAS_y.setObjectName("LBAS_y")
        self.horizontalLayout_5.addWidget(self.LBAS_y)
        self.set_LBAS = QtWidgets.QPushButton(Dialog)
        self.set_LBAS.setMaximumSize(QtCore.QSize(70, 16777215))
        self.set_LBAS.setObjectName("set_LBAS")
        self.horizontalLayout_5.addWidget(self.set_LBAS)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.nodes = QtWidgets.QListWidget(Dialog)
        self.nodes.setMinimumSize(QtCore.QSize(200, 236))
        self.nodes.setObjectName("nodes")
        self.verticalLayout_3.addWidget(self.nodes)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formation_label = QtWidgets.QLabel(Dialog)
        self.formation_label.setObjectName("formation_label")
        self.horizontalLayout_2.addWidget(self.formation_label)
        self.formations = QtWidgets.QComboBox(Dialog)
        self.formations.setObjectName("formations")
        self.formations.addItem("")
        self.formations.addItem("")
        self.formations.addItem("")
        self.formations.addItem("")
        self.formations.addItem("")
        self.formations.addItem("")
        self.horizontalLayout_2.addWidget(self.formations)
        self.night = QtWidgets.QCheckBox(Dialog)
        self.night.setObjectName("night")
        self.horizontalLayout_2.addWidget(self.night)
        self.retreat = QtWidgets.QCheckBox(Dialog)
        self.retreat.setObjectName("retreat")
        self.horizontalLayout_2.addWidget(self.retreat)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.side_label = QtWidgets.QLabel(Dialog)
        self.side_label.setObjectName("side_label")
        self.horizontalLayout_3.addWidget(self.side_label)
        self.side_x = QtWidgets.QSpinBox(Dialog)
        self.side_x.setMaximum(1919)
        self.side_x.setObjectName("side_x")
        self.horizontalLayout_3.addWidget(self.side_x)
        self.side_y = QtWidgets.QSpinBox(Dialog)
        self.side_y.setMaximum(1079)
        self.side_y.setObjectName("side_y")
        self.horizontalLayout_3.addWidget(self.side_y)
        self.set_side = QtWidgets.QPushButton(Dialog)
        self.set_side.setMaximumSize(QtCore.QSize(70, 16777215))
        self.set_side.setObjectName("set_side")
        self.horizontalLayout_3.addWidget(self.set_side)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.create_ = QtWidgets.QPushButton(Dialog)
        self.create_.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.create_.setFont(font)
        self.create_.setObjectName("create_")
        self.verticalLayout.addWidget(self.create_)
        self.delete_ = QtWidgets.QPushButton(Dialog)
        self.delete_.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_.setFont(font)
        self.delete_.setObjectName("delete_")
        self.verticalLayout.addWidget(self.delete_)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.void_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.void_2.sizePolicy().hasHeightForWidth())
        self.void_2.setSizePolicy(sizePolicy)
        self.void_2.setText("")
        self.void_2.setObjectName("void_2")
        self.verticalLayout_2.addWidget(self.void_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_5.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "查看地图"))
        self.label_3.setText(_translate("Dialog", "地图名："))
        self.LBAS_label.setText(_translate("Dialog", "基地航空队："))
        self.set_LBAS.setText(_translate("Dialog", "选取"))
        self.formation_label.setText(_translate("Dialog", "阵型："))
        self.formations.setItemText(0, _translate("Dialog", "单纵阵"))
        self.formations.setItemText(1, _translate("Dialog", "复纵阵"))
        self.formations.setItemText(2, _translate("Dialog", "梯形阵"))
        self.formations.setItemText(3, _translate("Dialog", "轮形阵"))
        self.formations.setItemText(4, _translate("Dialog", "单横阵"))
        self.formations.setItemText(5, _translate("Dialog", "警戒阵"))
        self.night.setText(_translate("Dialog", "夜战"))
        self.retreat.setText(_translate("Dialog", "撤退"))
        self.side_label.setText(_translate("Dialog", "分歧点："))
        self.set_side.setText(_translate("Dialog", "选取"))
        self.create_.setText(_translate("Dialog", "+"))
        self.delete_.setText(_translate("Dialog", "-"))
