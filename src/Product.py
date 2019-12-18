import os
import sys
import sqlite3
from forms.ProductForm import Ui_MainWindow
from PyQt5 import QtWidgets
from database import products_api
from database.projects_api import getProjectName
from database.systems_api import getSystemName
from modules.print_module import print_specification
from config import database_path, compiler

conn = sqlite3.connect(database_path)
cursor = conn.cursor()
answer = None

class ProductApp(QtWidgets.QMainWindow, Ui_MainWindow):
    Index = None
    SystemID = None
    UpdateFlag = None
    table_product = None
    Sum_product = None
    def __init__(self, System_id = None):
        print("Product app started with SystemID " + str(System_id))
        super().__init__()
        self.setupUi(self)
        self.SystemID = System_id
        self.loadData()
        self.Back_Button.clicked.connect(self.on_clicked_back)
        self.Print_Button.clicked.connect(self.print_docx)
        self.Update_Button.clicked.connect(self.update)
        self.LoadDB_Button.clicked.connect(self.loadData)
        self.Table.itemChanged.connect(self.cellChangedTable)
        self.Table.clicked.connect(self.on_ClickTable)
        #sort_by
        self.Price_Button.clicked.connect(self.sortTable)
        self.Number_Button.clicked.connect(self.sortTable)
        self.Code_Button.clicked.connect(self.sortTable)

    def sortTable(self):
        sender = self.sender()
        self.showTable(sort_by = sender.text())

    def price_sort(self,item):
        return int(item[2])
    def number_sort(self,item):
        return int(item[3])
    def code_sort(self,item):
        return int(item[0])


    def sum_update(self):
        self.Sum_product = 0
        for row in self.table_product:
            self.Sum_product += row[2]
        self.Sum_Label.setText("SUM: " + str(self.Sum_product))

    def loadData(self):
        self.table_product,sys,proj = products_api.loadProduct(self.SystemID)
        self.showTable()


    def showTable(self, sort_by = None):
        self.Table.setRowCount(0)
        if (sort_by == "Price"):
            self.table_product.sort(key=self.price_sort)
        elif (sort_by == "Number"):
            self.table_product.sort(key=self.number_sort)
        elif (sort_by == "Code"):
            self.table_product.sort(key=self.code_sort)
        #print(table)
        for row_number, row_data in enumerate(self.table_product):
            self.Table.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.Table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        self.sum_update()


    def on_ClickTable(self, item):
        self.Index = self.SearchIndexInTable(item.row(), item.column())
        #print(self.Index)

    def on_clicked_back(self):
        global answer
        answer = "back"
        self.close()

    def Update(self):
        self.UpdateFlag = True

    def cellChangedTable(self, item):
        if self.UpdateFlag == True:
            self.newItemText = item.text()

            #api.updateMain(self.newItemText, self.currentItemText, self.currentItemColumn,
                           #self.SearchIndexInTable(item.row(), item.column()))
            self.Update_all()
            self.UpdateFlag = False
        else:
            return

    def SearchIndexInTable(self, row, column):
        index_row = row
        index_column = 0
        return (self.Table.item(index_row, index_column).text())

    def print_docx(self):
        table_product, system_id, project_id = products_api.loadProduct(self.SystemID)
        rez = print_specification(getProjectName(project_id),getSystemName(system_id),table_product,sum=self.Sum_product)

        if(rez == 0):
            buttonReply = QtWidgets.QMessageBox.information(self, 'Print',
                                                            "Спецификация сохранена",
                                                            QtWidgets.QMessageBox.Ok)
        else:
            buttonReply = QtWidgets.QMessageBox.critical(self, 'Print',
                                                             "Ошибка сохранения спецификации",
                                                             QtWidgets.QMessageBox.Ok)

def Product(SystemIndex = None):
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ProductApp(SystemIndex)  # Создаём объект класса FirstWindowApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    if answer == "back":
        os.system(compiler + "System.py " + str(SystemIndex))



def main(arg = None):
    Product(arg)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()