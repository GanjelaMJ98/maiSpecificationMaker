# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProductForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(937, 617)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Table = QtWidgets.QTableWidget(self.centralwidget)
        self.Table.setGeometry(QtCore.QRect(40, 118, 841, 411))
        self.Table.setRowCount(15)
        self.Table.setColumnCount(8)
        self.Table.setObjectName("Table")
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(7, item)
        self.LoadDB_Button = QtWidgets.QPushButton(self.centralwidget)
        self.LoadDB_Button.setGeometry(QtCore.QRect(40, 78, 91, 31))
        self.LoadDB_Button.setObjectName("LoadDB_Button")
        self.Search_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Search_Button.setGeometry(QtCore.QRect(220, 78, 151, 31))
        self.Search_Button.setObjectName("Search_Button")
        self.Add_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Add_Button.setGeometry(QtCore.QRect(660, 78, 91, 31))
        self.Add_Button.setObjectName("Add_Button")
        self.Delete_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_Button.setGeometry(QtCore.QRect(520, 78, 91, 31))
        self.Delete_Button.setObjectName("Delete_Button")
        self.Update_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Update_Button.setGeometry(QtCore.QRect(760, 78, 91, 31))
        self.Update_Button.setObjectName("Update_Button")
        self.ID_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.ID_Text.setGeometry(QtCore.QRect(480, 78, 31, 31))
        self.ID_Text.setObjectName("ID_Text")
        self.ID_Label = QtWidgets.QLabel(self.centralwidget)
        self.ID_Label.setGeometry(QtCore.QRect(460, 80, 16, 21))
        self.ID_Label.setObjectName("ID_Label")
        self.Back_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_Button.setGeometry(QtCore.QRect(710, 570, 75, 23))
        self.Back_Button.setObjectName("Back_Button")
        self.Project_Lable = QtWidgets.QLabel(self.centralwidget)
        self.Project_Lable.setGeometry(QtCore.QRect(120, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Project_Lable.setFont(font)
        self.Project_Lable.setObjectName("Project_Lable")
        self.System_Label = QtWidgets.QLabel(self.centralwidget)
        self.System_Label.setGeometry(QtCore.QRect(540, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.System_Label.setFont(font)
        self.System_Label.setObjectName("System_Label")
        self.Print_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Print_Button.setGeometry(QtCore.QRect(800, 560, 91, 31))
        self.Print_Button.setObjectName("Print_Button")
        self.Code_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Code_Button.setGeometry(QtCore.QRect(420, 570, 75, 23))
        self.Code_Button.setObjectName("Code_Button")
        self.Number_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Number_Button.setGeometry(QtCore.QRect(500, 570, 75, 23))
        self.Number_Button.setObjectName("Number_Button")
        self.Price_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Price_Button.setGeometry(QtCore.QRect(580, 570, 75, 23))
        self.Price_Button.setObjectName("Price_Button")
        self.Sort_Label = QtWidgets.QLabel(self.centralwidget)
        self.Sort_Label.setGeometry(QtCore.QRect(500, 550, 47, 13))
        self.Sort_Label.setObjectName("Sort_Label")
        self.Sum_Label = QtWidgets.QLabel(self.centralwidget)
        self.Sum_Label.setGeometry(QtCore.QRect(130, 545, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.Sum_Label.setFont(font)
        self.Sum_Label.setObjectName("Sum_Label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Code"))
        item = self.Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product"))
        item = self.Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Number"))
        item = self.Table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Contractor"))
        item = self.Table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fabricator"))
        item = self.Table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Currency"))
        item = self.Table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Delivery"))
        self.LoadDB_Button.setText(_translate("MainWindow", "Load DB"))
        self.Search_Button.setText(_translate("MainWindow", "Search"))
        self.Add_Button.setText(_translate("MainWindow", "ADD"))
        self.Delete_Button.setText(_translate("MainWindow", "DELETE"))
        self.Update_Button.setText(_translate("MainWindow", "UPDATE"))
        self.ID_Label.setText(_translate("MainWindow", "ID"))
        self.Back_Button.setText(_translate("MainWindow", "Back"))
        self.Project_Lable.setText(_translate("MainWindow", "Project: Самолёт"))
        self.System_Label.setText(_translate("MainWindow", "System: Фюзеляж"))
        self.Print_Button.setText(_translate("MainWindow", "PRINT"))
        self.Code_Button.setText(_translate("MainWindow", "Code"))
        self.Number_Button.setText(_translate("MainWindow", "Number"))
        self.Price_Button.setText(_translate("MainWindow", "Price"))
        self.Sort_Label.setText(_translate("MainWindow", "Sort by"))
        self.Sum_Label.setText(_translate("MainWindow", "TextLabel"))

