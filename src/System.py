# -*- coding: utf8 -*-
import sys
import sqlite3
from forms.SystemForm import Ui_MainWindow
from PyQt5 import QtWidgets
from database import systems_api
from Product import Product

conn = sqlite3.connect("D:\Code\Git\maiSpecificationMaker\Specifications.sqlite")
cursor = conn.cursor()
answer = None

class SystemApp(QtWidgets.QMainWindow, Ui_MainWindow):
    Index = None
    def __init__(self, Project_id = None):
        super().__init__()
        self.setupUi(self)
        self.AddButton.clicked.connect(self.on_clicked_add)
        self.BackButton.clicked.connect(self.on_clicked_back)
        self.OkButton.clicked.connect(self.on_clicked_ok)
        self.loadData(Project_id)
        self.table.clicked.connect(self.on_ClickTable)
        #self.table.itemChanged.connect(self.cell_changed_table)

    def on_clicked_add(self):
        self.close()

    def on_clicked_ok(self):
        if self.Index is not None:
            global answer
            answer = self.Index
            self.close()
        else:
            print("error")

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
    print("systemstart" + str(ProjectIndex))
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = SystemApp(ProjectIndex)  # Создаём объект класса FirstWindowApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    if answer == "back":
        window.close()
        app.quit()
        return answer
    else:
        Product(answer)

def main():
    System()

if __name__ == "__main__":
   main()