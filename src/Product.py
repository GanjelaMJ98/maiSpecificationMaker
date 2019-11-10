import sys
import sqlite3
from forms.ProductForm import Ui_MainWindow
from PyQt5 import QtWidgets
from database import products_api
conn = sqlite3.connect("D:\Code\Git\maiSpecificationMaker\Specifications.sqlite")
cursor = conn.cursor()
answer = None
#TODO:
class ProductApp(QtWidgets.QMainWindow, Ui_MainWindow):
    Index = None
    SystemID = None
    def __init__(self, System_id = None):
        super().__init__()
        self.setupUi(self)
        self.loadData(System_id)
        #self.Back_but.clicked.connect(self.on_clicked_back)
        self.Back_but.clicked.connect(self.print_docx)
        #self.table.clicked.connect(on_ClickTable)
        #self.table.itemChanged.connect(self.cell_changed_table)


    def loadData(self, System_id = None):
        res,sys,proj = products_api.loadProduct(System_id)
        self.SystemID = sys
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.table.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

    def on_ClickTable(self, item):
        self.Index = self.SearchIndexInTable(item.row(), item.column())
        #print(self.Index)

    def on_clicked_back(self):
        global answer
        answer = "back"
        self.close()

    def print_docx(self):
        res, sys, proj = products_api.loadProduct(self.SystemID)
        print(res)
        print(sys)
        print(proj)

def Product(SystemIndex = None):
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ProductApp(SystemIndex)  # Создаём объект класса FirstWindowApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    if answer == "back":
        return(answer)
    else:
        pass




def main():
    Product(1)

if __name__ == "__main__":
   main()