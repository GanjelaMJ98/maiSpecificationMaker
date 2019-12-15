# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SystemForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_System(object):
    def setupUi(self, System):
        System.setObjectName("System")
        System.resize(341, 547)
        self.centralwidget = QtWidgets.QWidget(System)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.table)
        self.UpdateButton = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateButton.setObjectName("UpdateButton")
        self.verticalLayout.addWidget(self.UpdateButton)
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setObjectName("BackButton")
        self.verticalLayout.addWidget(self.BackButton)
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setObjectName("AddButton")
        self.verticalLayout.addWidget(self.AddButton)
        self.OkButton = QtWidgets.QPushButton(self.centralwidget)
        self.OkButton.setObjectName("OkButton")
        self.verticalLayout.addWidget(self.OkButton)
        System.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(System)
        self.statusbar.setObjectName("statusbar")
        System.setStatusBar(self.statusbar)

        self.retranslateUi(System)
        QtCore.QMetaObject.connectSlotsByName(System)

    def retranslateUi(self, System):
        _translate = QtCore.QCoreApplication.translate
        System.setWindowTitle(_translate("System", "MainWindow"))
        self.label.setText(_translate("System", "Systems"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("System", "id"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("System", "System"))
        self.UpdateButton.setText(_translate("System", "Update"))
        self.BackButton.setText(_translate("System", "Back"))
        self.AddButton.setText(_translate("System", "ADD"))
        self.OkButton.setText(_translate("System", "Ok"))

