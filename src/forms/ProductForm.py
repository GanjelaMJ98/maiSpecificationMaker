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
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(40, 118, 841, 411))
        self.table.setRowCount(15)
        self.table.setColumnCount(8)
        self.table.setObjectName("table")
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        self.LoadDB_but = QtWidgets.QPushButton(self.centralwidget)
        self.LoadDB_but.setGeometry(QtCore.QRect(40, 78, 91, 31))
        self.LoadDB_but.setObjectName("LoadDB_but")
        self.Search_but = QtWidgets.QPushButton(self.centralwidget)
        self.Search_but.setGeometry(QtCore.QRect(220, 78, 151, 31))
        self.Search_but.setObjectName("Search_but")
        self.Add_but = QtWidgets.QPushButton(self.centralwidget)
        self.Add_but.setGeometry(QtCore.QRect(660, 78, 91, 31))
        self.Add_but.setObjectName("Add_but")
        self.Delete_but = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_but.setGeometry(QtCore.QRect(520, 78, 91, 31))
        self.Delete_but.setObjectName("Delete_but")
        self.Update_but = QtWidgets.QPushButton(self.centralwidget)
        self.Update_but.setGeometry(QtCore.QRect(760, 78, 91, 31))
        self.Update_but.setObjectName("Update_but")
        self.ID_t = QtWidgets.QLineEdit(self.centralwidget)
        self.ID_t.setGeometry(QtCore.QRect(480, 78, 31, 31))
        self.ID_t.setObjectName("ID_t")
        self.id_l = QtWidgets.QLabel(self.centralwidget)
        self.id_l.setGeometry(QtCore.QRect(460, 80, 16, 21))
        self.id_l.setObjectName("id_l")
        self.Back_but = QtWidgets.QPushButton(self.centralwidget)
        self.Back_but.setGeometry(QtCore.QRect(20, 560, 75, 23))
        self.Back_but.setObjectName("Back_but")
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
        item.setText(_translate("MainWindow", "Code"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Number"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Contractor"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fabricator"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Currency"))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Delivery"))
        self.LoadDB_but.setText(_translate("MainWindow", "Load DB"))
        self.Search_but.setText(_translate("MainWindow", "Search"))
        self.Add_but.setText(_translate("MainWindow", "ADD"))
        self.Delete_but.setText(_translate("MainWindow", "DELETE"))
        self.Update_but.setText(_translate("MainWindow", "UPDATE"))
        self.id_l.setText(_translate("MainWindow", "ID"))
        self.Back_but.setText(_translate("MainWindow", "Back"))

