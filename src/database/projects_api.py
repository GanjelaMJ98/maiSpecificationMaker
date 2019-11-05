import sqlite3

conn = sqlite3.connect('Specifications.sqlite')
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
        return 1
    else:
        print("Project already exists")
        conn.commit()
        return 0

def updateProject(project_id, project_name):
    sql = "UPDATE Projects_t SET project_name = {0} WHERE project_id = {1}".format(
            project_name, project_id)
    cursor.execute(sql)
    conn.commit()
    return 0


def test():
    addProject("Airplane")
    addProject("Building")
    print(getProjectID("Airplane"))



if __name__ == "__main__":
   test()