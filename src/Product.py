import sys
import sqlite3
from forms.ProductForm import Ui_MainWindow
from PyQt5 import QtWidgets
from database import systems_api
conn = sqlite3.connect("D:\Code\Git\maiSpecificationMaker\Specifications.sqlite")
cursor = conn.cursor()
answer = None
#TODO:
class ProductApp(QtWidgets.QMainWindow, Ui_MainWindow):
    Index = None
    def __init__(self, Project_id = None):
        super().__init__()
        self.setupUi(self)
        self.loadData(System_id)
        #self.table.clicked.connect(on_ClickTable)
        #self.table.itemChanged.connect(self.cell_changed_table)


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
        #print(self.Index)



def Product(SystemIndex = None):
    print("systemstart" + str(ProjectIndex))
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ProductApp(ProjectIndex)  # Создаём объект класса FirstWindowApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    if answer == "back":
        return(answer)
    else:
        System(answer)

def main():
    Product()

if __name__ == "__main__":
   main()