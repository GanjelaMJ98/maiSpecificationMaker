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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartCreate_but = QtWidgets.QPushButton(self.centralwidget)
        self.StartCreate_but.setGeometry(QtCore.QRect(210, 60, 341, 71))
        self.StartCreate_but.setObjectName("StartCreateButton")
        self.StartUpdate_but = QtWidgets.QPushButton(self.centralwidget)
        self.StartUpdate_but.setGeometry(QtCore.QRect(210, 190, 341, 71))
        self.StartUpdate_but.setObjectName("StartUpdateButton")
        self.StartPrint_but = QtWidgets.QPushButton(self.centralwidget)
        self.StartPrint_but.setGeometry(QtCore.QRect(210, 320, 341, 71))
        self.StartPrint_but.setObjectName("StartPrintButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.StartCreate_but.setText(_translate("MainWindow", "Create"))
        self.StartUpdate_but.setText(_translate("MainWindow", "Update"))
        self.StartPrint_but.setText(_translate("MainWindow", "Print"))

