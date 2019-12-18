# -*- coding: utf8 -*-
import os
import sys
import sqlite3
from forms.SystemForm import Ui_System
from PyQt5 import QtWidgets
from database import systems_api
from config import database_path, compiler
from Product import Product, ProductApp

conn = sqlite3.connect(database_path)
cursor = conn.cursor()
answer = None

class SystemApp(QtWidgets.QMainWindow, Ui_System):
    Index = None
    def __init__(self, Project_id = None):
        super().__init__()
        self.Project_ID = Project_id
        self.setupUi(self)
        self.AddButton.clicked.connect(self.on_clicked_add)
        self.BackButton.clicked.connect(self.on_clicked_back)
        self.OkButton.clicked.connect(self.on_clicked_ok)
        self.loadData(Project_id)
        self.table.clicked.connect(self.on_ClickTable)
        #self.table.itemChanged.connect(self.cell_changed_table)

    def on_clicked_add(self):
        self.close()
        os.system(compiler + "AddSystem.py " + str(self.Project_ID))


    def on_clicked_ok(self):
        if self.Index is not None:
            self.close()  # закрываем окно
            os.system(compiler + "Product.py " + str(self.Index))  # вызываем следующее (КОСТЫЛЬ)
        else:
            buttonReply = QtWidgets.QMessageBox.critical(self, 'System error',
                                                         "Необходимо выбрать систему для продолжения",
                                                         QtWidgets.QMessageBox.Ok)

    def on_clicked_back(self):
        global answer
        answer = "back"
        self.close()

    def loadData(self, Project_id = None):
        sql = systems_api.loadSystem(Project_id)
        res = conn.execute(sql)
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.table.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

    def on_ClickTable(self, item):
        self.Index = self.SearchIndexInTable(item.row(), item.column())
        print(self.Index)

    def SearchIndexInTable(self, row, column):
        index_row = row
        index_column = 0
        return (self.table.item(index_row, index_column).text())

def System(ProjectIndex = None):

    #print("systemstart" + str(ProjectIndex))
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = SystemApp(ProjectIndex)  # Создаём объект класса FirstWindowApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    if answer == "back":
        os.system(compiler + "Project.py")
        #window.close()
        #app.quit()
        #return answer


def main(arg = None):
    System(arg)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()