# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(297, 493)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Project_name_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Project_name_text.setGeometry(QtCore.QRect(30, 320, 151, 21))
        self.Project_name_text.setObjectName("Project_name_text")
        self.Create_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Create_Button.setGeometry(QtCore.QRect(180, 320, 75, 23))
        self.Create_Button.setObjectName("Create_Button")
        self.H1 = QtWidgets.QLabel(self.centralwidget)
        self.H1.setGeometry(QtCore.QRect(60, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.H1.setFont(font)
        self.H1.setObjectName("H1")
        self.H2 = QtWidgets.QLabel(self.centralwidget)
        self.H2.setGeometry(QtCore.QRect(30, 290, 71, 20))
        self.H2.setObjectName("H2")
        self.Back_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_Button.setGeometry(QtCore.QRect(30, 390, 75, 23))
        self.Back_Button.setObjectName("Back_Button")
        self.Error_lable = QtWidgets.QLabel(self.centralwidget)
        self.Error_lable.setGeometry(QtCore.QRect(10, 180, 311, 21))
        self.Error_lable.setText("")
        self.Error_lable.setObjectName("Error_lable")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(40, 80, 201, 192))
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.Ok_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Ok_Button.setGeometry(QtCore.QRect(180, 390, 75, 23))
        self.Ok_Button.setObjectName("Ok_Button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Create_Button.setText(_translate("MainWindow", "Create"))
        self.H1.setText(_translate("MainWindow", "Create Project"))
        self.H2.setText(_translate("MainWindow", "Project Name"))
        self.Back_Button.setText(_translate("MainWindow", "Back"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Project"))
        self.Ok_Button.setText(_translate("MainWindow", "Ok"))
