# -*- coding: utf8 -*-
import sys
sys.path.insert(1, 'D:\Code\Git\maiSpecificationMaker')

from modules.auth_module import authentication
from FirstWindow import FirstWindow
from Project import Project
from System import System

def main():
    print("Start")
    name, status = authentication(test = 1)
    print("User: " + str(name) + " with status " +str(status))
    while(1):
        rez = Project()
        print("Project answer = " + str(rez))
        if rez == "stop":
            break


if __name__ == "__main__":
   main()