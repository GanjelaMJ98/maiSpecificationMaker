# -*- coding: utf8 -*-
import os
import sys
import sqlite3
from forms.ProjectForm import Ui_MainWindow
from PyQt5 import QtWidgets
from database import projects_api
import time as t
from System import System, SystemApp

answer = None
conn = sqlite3.connect("D:\Code\Git\maiSpecificationMaker\Specifications.sqlite")
cursor = conn.cursor()


class ProjectApp(QtWidgets.QMainWindow, Ui_MainWindow):
    textProjectName = list()
    currentProjectName = None
    Index = None


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Create_Button.clicked.connect(self.on_clicked_create)
        self.Back_Button.clicked.connect(self.on_clicked_back)
        self.Ok_Button.clicked.connect(self.on_clicked_ok)
        self.Project_name_text.textChanged.connect(self.onTextProjectName)
        self.loadData()
        self.table.clicked.connect(self.on_ClickTable)

    def loadData(self):
        sql = projects_api.loadProjects()
        res = conn.execute(sql)
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.table.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

    def on_clicked_create(self):
        if(self.currentProjectName is None or self.currentProjectName == ""):
            buttonReply = QtWidgets.QMessageBox.critical(self, 'Project error',
                                                         "Введите название проекта для добавления",
                                                         QtWidgets.QMessageBox.Ok)

        else:
            db_ans = projects_api.addProject(self.currentProjectName)
            if(db_ans == 0):
                self.loadData()
                buttonReply = QtWidgets.QMessageBox.information(self, 'Project',
                                                             "Проект добавлен: "+ str(self.currentProjectName),QtWidgets.QMessageBox.Ok)

            else:
                buttonReply = QtWidgets.QMessageBox.critical(self, 'Project error',
                                                             db_ans,
                                                             QtWidgets.QMessageBox.Ok)

            t.sleep(1)

    def on_clicked_back(self):
        global answer
        answer = "back"
        self.close()


    def on_clicked_ok(self):
        if self.Index is not None:
            self.close()                                        #закрываем окно
            os.system("python System.py " + str(self.Index))    #вызываем следующее (КОСТЫЛЬ)
        else:
            buttonReply = QtWidgets.QMessageBox.critical(self, 'Project error', "Необходимо выбрать проект для продолжения",
                                               QtWidgets.QMessageBox.Ok)
            #print(int(buttonReply))
            #if buttonReply == QtWidgets.QMessageBox.Ok:
               # print('Yes clicked.')


    def onTextProjectName(self, text):
        self.textProjectName.append(text)
        self.currentProjectName = self.textProjectName[-1]


    def on_ClickTable(self, item):
        self.Index = self.SearchIndexInTable(item.row(), item.column())
        #print(self.Index)

    def SearchIndexInTable(self, row, column):
        index_row = row
        index_column = 0
        return (self.table.item(index_row, index_column).text())



def Project():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ProjectApp()  # Создаём объект класса FirstWindowApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    window.close()
    app.quit()



def main():
    Project()

if __name__ == "__main__":
   main()