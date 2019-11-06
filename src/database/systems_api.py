import sqlite3
from projects_api import addProject, getProjectID


conn = sqlite3.connect("Specifications.sqlite")
cursor = conn.cursor()

def getSystemID(system_name):
    sql = "SELECT id FROM Systems_t WHERE system_name = '{0}'".format(system_name)
    for ans in cursor.execute(sql):
        return ans[0]
        #TODO: Добавить проверку на Null

def addSystem(system_name, project_name):
    addProject(project_name)
    n = False
    for row in cursor.execute("SELECT * from Systems_t"):
        if row[1] == system_name:
            n = True
    if n == False:
        project_sql = "(SELECT id FROM Projects_t WHERE project_name =  '{0}')".format(project_name)
        sql = "INSERT INTO Systems_t VALUES (NULL,'{0}',{1}) ".format(system_name, project_sql)
        cursor.execute(sql)
        print("Added system ", system_name)
        conn.commit()
        return 1
    else:
        print("System already exists")
        conn.commit()
        return 0


def updateSystem(system_id, system_name,project_name = None):
    if project_name is not None:
        project_id = getProjectID()
        sql = "UPDATE Systems_t SET system_name = {0}, project_id = {1} WHERE system_id = {2}".format(
            system_name,project_id,system_id)
    else:
        sql = "UPDATE Systems_t SET system_name = {0} WHERE system_id = {1}".format(
            system_name, system_id)
    cursor.execute(sql)
    conn.commit()
    return 0



if __name__ == "__main__":
    addSystem("SU", "Airplane")
    addSystem("Fundament", "Building")
    conn.commit()
