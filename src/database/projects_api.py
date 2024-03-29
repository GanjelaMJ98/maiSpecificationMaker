# -*- coding: utf8 -*-
import sqlite3
from config import database_path
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

def getProjectName(project_id):
    sql = "SELECT project_name FROM Projects_t WHERE id = '{0}'".format(project_id)
    for ans in cursor.execute(sql):
        return ans[0]
        #TODO: Добавить проверку на Null

def getProjectID(project_name):
    sql = "SELECT id FROM Projects_t WHERE project_name = '{0}'".format(project_name)
    for ans in cursor.execute(sql):
        return ans[0]
        #TODO: Добавить проверку на Null

def addProject(project_name):
    n = False
    for row in cursor.execute("SELECT * from Projects_t"):
        if row[1] == project_name:
            n = True
    if n == False:
        cursor.execute("INSERT INTO Projects_t VALUES (NULL,?) ", [project_name] )
        print("Added project ", project_name)
        conn.commit()
        return 0
    else:
        print("Project already exists")
        conn.commit()
        return "Project already exists"

def updateProject(project_id, project_name):
    sql = "UPDATE Projects_t SET project_name = {0} WHERE project_id = {1}".format(
            project_name, project_id)
    cursor.execute(sql)
    conn.commit()
    return 0

def loadProjects(name = None, id = None):
    list = []
    if name is not None:
        sql = "SELECT * FROM Projects_t WHERE project_name ='{0}'".format(name)
    elif id is not None:
        sql = "SELECT * FROM Projects_t WHERE id ='{0}'".format(id)
    else:
        sql = "SELECT * FROM Projects_t"
    #for row in cursor.execute(sql):
        #list.append(row)
    #print(list)
    return sql




if __name__ == "__main__":
    addProject("Airplane")
    addProject("Building")
    print(getProjectID("Airplane"))
    loadProject("Airplane")