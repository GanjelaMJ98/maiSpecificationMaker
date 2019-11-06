import sqlite3
from projects_api import addProject
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


if __name__ == "__main__":
    addProduct("Monitor", 10000, 10, "MAI", "DNS","LOL","HOMA")
    conn.commit()