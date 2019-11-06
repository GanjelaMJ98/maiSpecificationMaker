# -*- coding: utf8 -*-
import sys
sys.path.insert(1, 'D:\старый комп\со старого компьютера\Документы\Паша\МАИ\4 курс\Максимов\maiSpecificationMaker')
sys.path.append('../GUI/forms')
from modules.auth_module import authentication
from FirstWindow import FirstWindow
from CreateProject import CreateProject

def main():
    print("Start")
    name, status = authentication(test = 1)
    print("User: " + str(name) + " with status " +str(status))
    start = FirstWindow()
    print(str(name) + " selected " + str(start))
    if(start == "Create"):
        CreateProject()


if __name__ == "__main__":
   main()