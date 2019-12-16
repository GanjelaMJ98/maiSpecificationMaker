# -*- coding: utf8 -*-
import os
import sys
import sqlite3
import time
from forms.AddSystemForm import Ui_MainWindow
from PyQt5 import QtWidgets
from database import systems_api
from database import projects_api


conn = sqlite3.connect("D:\Code\Git\maiSpecificationMaker\Specifications.sqlite")
cursor = conn.cursor()
answer = None

class AddSystemApp(QtWidgets.QMainWindow, Ui_MainWindow):
    Index = None
    textProject = list()
    textSystem = list()
    currentProject = str()
    currentSystem = str()
    projects_list = []
    def __init__(self, Project_id = None):
        self.Project_ID = Project_id
        super().__init__()
        self.setupUi(self)
        self.Add_Button.clicked.connect(self.on_clicked_add)
        self.Cancel_Button.clicked.connect(self.on_clicked_cancel)
        self.System_Text.textChanged.connect(self.onSystemText)
        self.updateComboBox()

    def onSystemText(self, text):
        self.textSystem.append(text)
        self.currentSystem = self.textSystem[-1]

    def onProjectText(self, text):
        self.textProject.append(text)
        self.currentProject = self.textProject[-1]

    def on_clicked_add(self):
        if(self.projects_list.count(self.currentProject) == 0):
            print("Недопустимый проект")
        elif(self.currentSystem is None or self.currentSystem == ""):
            print("Пустая система")
        else:
            ans = systems_api.addSystem(self.currentSystem, self.currentProject)
            if (ans == 0):
                buttonReply = QtWidgets.QMessageBox.critical(self, 'System error',
                                                             "System already exists",
                                                             QtWidgets.QMessageBox.Ok)
            elif(ans == 1):
                buttonReply = QtWidgets.QMessageBox.information(self, 'System error',
                                                             "Added system",
                                                             QtWidgets.QMessageBox.Ok)
        os.system("python System.py " + str(self.Project_ID))



    def on_clicked_cancel(self):
        self.close()

    def updateComboBox(self):
        self.Project_Box.clear()
        projects_sql = projects_api.loadProjects(id = self.Project_ID)
        for row in cursor.execute(projects_sql):
            self.projects_list.append(row[1])
        for project in self.projects_list:
            self.Project_Box.addItem(project)
            self.currentProject = project
        self.Project_Box.activated[str].connect(self.TextUpdateProject)

    def TextUpdateProject(self, text):
        self.Project_Text.setText(text)
        self.currentProject = text




def AddSystem(ProjectIndex = None):
    #print("systemstart" + str(ProjectIndex))
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = AddSystemApp(ProjectIndex)  # Создаём объект класса FirstWindowApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    if answer == "back":
        os.system("python Project.py")
        #window.close()
        #app.quit()
        #return answer


def main(arg = None):
    AddSystem(arg)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()