# -*- coding: utf8 -*-
import sys
sys.path.insert(1, 'D:\Code\Git\maiSpecificationMaker')

from modules.auth_module import authentication
from FirstWindow import FirstWindow
from Project import Project
from System import System

def main():
    print("Start")
    name, status = authentication()
    print("User: " + str(name) + " with status " +str(status))
    Project()


if __name__ == "__main__":
   main()