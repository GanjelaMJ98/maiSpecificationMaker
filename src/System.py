# -*- coding: utf8 -*-
import sys
import sqlite3
from forms.SystemForm import Ui_MainWindow
from PyQt5 import QtWidgets
from database import systems_api
conn = sqlite3.connect("D:\Code\Git\maiSpecificationMaker\Specifications.sqlite")
cursor = conn.cursor()
answer = None

class SystemApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.AddButton.clicked.connect(self.on_clicked_add)
        self.BackButton.clicked.connect(self.loadData)
        #self.table.clicked.connect(self.loadData)
        #self.table.itemChanged.connect(self.cell_changed_table)
    def on_clicked_add(self):
        self.close()

    def on_clicked_back(self):
        global answer
        answer = "Back"
        self.close()

    def loadData(self):
        sql = systems_api.loadSystem()
        res = conn.execute(sql)
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.table.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))




def System():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = SystemApp()  # Создаём объект класса FirstWindowApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


def main():
    print(System())

if __name__ == "__main__":
   main()