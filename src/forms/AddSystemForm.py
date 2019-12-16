# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddSystemForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(324, 284)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Project_Label = QtWidgets.QLabel(self.centralwidget)
        self.Project_Label.setGeometry(QtCore.QRect(40, 10, 47, 13))
        self.Project_Label.setObjectName("Project_Label")
        self.Project_Box = QtWidgets.QComboBox(self.centralwidget)
        self.Project_Box.setGeometry(QtCore.QRect(40, 80, 241, 21))
        self.Project_Box.setObjectName("Project_Box")
        self.Add_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Add_Button.setGeometry(QtCore.QRect(60, 230, 75, 23))
        self.Add_Button.setObjectName("Add_Button")
        self.Cancel_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel_Button.setGeometry(QtCore.QRect(180, 230, 75, 23))
        self.Cancel_Button.setObjectName("Cancel_Button")
        self.System_Label = QtWidgets.QLabel(self.centralwidget)
        self.System_Label.setGeometry(QtCore.QRect(40, 120, 47, 13))
        self.System_Label.setObjectName("System_Label")
        self.Project_Text = QtWidgets.QTextBrowser(self.centralwidget)
        self.Project_Text.setGeometry(QtCore.QRect(40, 50, 241, 31))
        self.Project_Text.setObjectName("Project_Text")
        self.System_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.System_Text.setGeometry(QtCore.QRect(40, 160, 241, 31))
        self.System_Text.setObjectName("System_Text")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Project_Label.setText(_translate("MainWindow", "Project"))
        self.Add_Button.setText(_translate("MainWindow", "Add"))
        self.Cancel_Button.setText(_translate("MainWindow", "Cancel"))
        self.System_Label.setText(_translate("MainWindow", "System"))

