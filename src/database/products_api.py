import sqlite3
#from projects_api import addProject
import sqlite3

conn = sqlite3.connect("D:\Code\Git\maiSpecificationMaker\Specifications.sqlite")
cursor = conn.cursor()

def getProductID(product_name):
    sql = "SELECT id FROM Products_t WHERE product_name = '{0}'".format(product_name)
    for ans in cursor.execute(sql):
        return ans[0]
        #TODO: Добавить проверку на Null


def addProduct(product_name,price,number,contractor,fabricator,currency,delivery):
    n = False
    for row in cursor.execute("SELECT * from Products_t"):
        if row[1] == product_name:
            n = True
    if n == False:
        sql = "INSERT INTO Products_t VALUES (NULL,'{0}',{1},{}) ".format(system_name, project_sql)
        cursor.execute(sql)
        print("Added product ", product_name)
        conn.commit()
        return 1
    else:
        print("Product already exists")
        conn.commit()
        return 0

def loadSubsystem(system_id):
    #list = []
    if system_id is not None:
        sql = "SELECT * FROM Subsystems_t WHERE system_id = '{0}'".format(system_id)
    else:
        sql = "SELECT * FROM Subsystems_t"
    #for row in cursor.execute(sql):
        #list.append(row)
    #print(list)
    return sql

def loadProduct(system = None):
    project_id = None
    product_list = []
    subsystem_list = []
    subsystem_sql = loadSubsystem(system)
    for row in cursor.execute(subsystem_sql):
        subsystem_list.append(row)
    print(subsystem_list)
    for row in subsystem_list:
        sql = "SELECT * FROM Products_t WHERE id = '{0}'".format(row[2])
        project_id = row[3]
        for r in cursor.execute(sql):
            # меняем number(product) на sum(subsystem)
            r = list(r)
            r[3] = row[2]
            product_list.append(r)
    #print(product_list)
    return product_list , system ,project_id
    #if project is not None:
        #sql = "SELECT id, system_name FROM Systems_t WHERE project_id = '{0}'".format(project)
    #else:
        #sql = "SELECT id, system_name FROM Systems_t"
    #for row in cursor.execute(sql):
        #list.append(row)
    #print(list)
    #return sql


if __name__ == "__main__":
    #addProduct("Monitor", 10000, 10, "MAI", "DNS","LOL","HOMA")
    #conn.commit()
    loadProduct(1)