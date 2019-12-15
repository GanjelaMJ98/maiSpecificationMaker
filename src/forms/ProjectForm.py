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
        MainWindow.resize(268, 558)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.H1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.H1.setFont(font)
        self.H1.setObjectName("H1")
        self.verticalLayout.addWidget(self.H1)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.table)
        self.H2 = QtWidgets.QLabel(self.centralwidget)
        self.H2.setObjectName("H2")
        self.verticalLayout.addWidget(self.H2)
        self.Project_name_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Project_name_text.setObjectName("Project_name_text")
        self.verticalLayout.addWidget(self.Project_name_text)
        self.Error_lable = QtWidgets.QLabel(self.centralwidget)
        self.Error_lable.setText("")
        self.Error_lable.setObjectName("Error_lable")
        self.verticalLayout.addWidget(self.Error_lable)
        self.Create_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Create_Button.setObjectName("Create_Button")
        self.verticalLayout.addWidget(self.Create_Button)
        self.Ok_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Ok_Button.setObjectName("Ok_Button")
        self.verticalLayout.addWidget(self.Ok_Button)
        self.Back_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_Button.setObjectName("Back_Button")
        self.verticalLayout.addWidget(self.Back_Button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.H1.setText(_translate("MainWindow", "Create Project"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Project"))
        self.H2.setText(_translate("MainWindow", "Project Name"))
        self.Create_Button.setText(_translate("MainWindow", "Create"))
        self.Ok_Button.setText(_translate("MainWindow", "Ok"))
        self.Back_Button.setText(_translate("MainWindow", "Back"))

