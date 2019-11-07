# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SystemForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(20, 100, 301, 331))
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(240, 460, 75, 23))
        self.AddButton.setObjectName("AddButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(30, 460, 75, 23))
        self.BackButton.setObjectName("BackButton")
        self.UpdateButton = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateButton.setGeometry(QtCore.QRect(130, 460, 75, 23))
        self.UpdateButton.setObjectName("UpdateButton")
        self.OkButton = QtWidgets.QPushButton(self.centralwidget)
        self.OkButton.setGeometry(QtCore.QRect(240, 500, 75, 23))
        self.OkButton.setObjectName("OkButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "System"))
        self.label.setText(_translate("MainWindow", "Systems"))
        self.AddButton.setText(_translate("MainWindow", "ADD"))
        self.BackButton.setText(_translate("MainWindow", "Back"))
        self.UpdateButton.setText(_translate("MainWindow", "Update"))
        self.OkButton.setText(_translate("MainWindow", "Ok"))

