from setuptools import setup, find_packages
from config import database_path, compiler
import os
os.system(compiler +" CreateDB.py")
setup(name='maiSpecificationMaker', version='1.0', packages=find_packages())