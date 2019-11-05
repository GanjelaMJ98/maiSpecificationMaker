# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstWindowForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(592, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartCreateButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartCreateButton.setGeometry(QtCore.QRect(120, 40, 341, 71))
        self.StartCreateButton.setObjectName("StartCreateButton")
        self.StartUpdateButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartUpdateButton.setGeometry(QtCore.QRect(120, 130, 341, 71))
        self.StartUpdateButton.setObjectName("StartUpdateButton")
        self.StartPrintButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartPrintButton.setGeometry(QtCore.QRect(120, 220, 341, 71))
        self.StartPrintButton.setObjectName("StartPrintButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 592, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartCreateButton.setText(_translate("MainWindow", "Create"))
        self.StartUpdateButton.setText(_translate("MainWindow", "Update"))
        self.StartPrintButton.setText(_translate("MainWindow", "Print"))

