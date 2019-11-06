# -*- coding: utf8 -*-
import sys
sys.path.insert(1, 'D:\Code\Git\maiSpecificationMaker')

from modules.auth_module import authentication
from FirstWindow import FirstWindow
from Project import Project

def main():
    print("Start")
    name, status = authentication(test = 1)
    print("User: " + str(name) + " with status " +str(status))
    start = FirstWindow()
    print(str(name) + " selected " + str(start))
    if(start == "Create"):
        Project()


if __name__ == "__main__":
   main()