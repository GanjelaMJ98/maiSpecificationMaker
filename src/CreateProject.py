# -*- coding: utf8 -*-
import sys
from forms.CreateProjectForm import Ui_MainWindow
from PyQt5 import QtWidgets
from database import projects_api

answer = None

class CreateProjectApp(QtWidgets.QMainWindow, Ui_MainWindow):
    textProjectName = list()
    currentProjectName = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.CreateButton.clicked.connect(self.on_clicked_create)
        self.BackButton.clicked.connect(self.on_clicked_back)
        self.Project_name_text.textChanged.connect(self.onTextProjectName)

    def on_clicked_create(self):
        if(self.currentProjectName is None or self.currentProjectName == ""):
            self.Error_lable.setText("Error")
        else:
            db_ans = projects_api.addProject(self.currentProjectName)
            self.Error_lable.setText(db_ans)
            self.close()

    def on_clicked_back(self):
        self.close()

    def onTextProjectName(self, text):
        self.textProjectName.append(text)
        self.currentProjectName = self.textProjectName[-1]




def CreateProject():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = CreateProjectApp()  # Создаём объект класса FirstWindowApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


def main():
    print(CreateProject())

if __name__ == "__main__":
   main()