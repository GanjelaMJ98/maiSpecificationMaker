# -*- coding: utf8 -*-
import sqlite3

conn = sqlite3.connect("D:\Code\Git\maiSpecificationMaker\Specifications.sqlite")
cursor = conn.cursor()

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
        return "Added project "+ project_name
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

def loadProjects(name = None):
    list = []
    if name is not None:
        sql = "SELECT * FROM Projects_t WHERE project_name ='{0}'".format(name)
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