import sqlite3

conn = sqlite3.connect('Specifications.sqlite')
cursor = conn.cursor()


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

def test():
    addProject("Airplane")
    addProject("Building")



if __name__ == "__main__":
   test()