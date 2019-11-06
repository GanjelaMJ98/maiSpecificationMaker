import sqlite3
from projects_api import addProject
from systems_api import getSystemID
from products_api import getProductID

conn = sqlite3.connect("D:\Code\Git\maiSpecificationMaker\Specifications.sqlite")
cursor = conn.cursor()
def getProductSUM(product_id):
    sql = "SELECT sum FROM Subsystems_t WHERE product_id = '{0}'".format(product_id)
    for ans in cursor.execute(sql):
        return ans[0]
        #TODO: Добавить проверку нa NULL

def addSubsystem(system_name, product_name, product_sum):
    n = False
    system_id = getSystemID(system_name)
    product_id = getProductID(product_name)
    for row in cursor.execute("SELECT * FROM Subsystems_t WHERE system_id = ({0}) AND product_id = ({1})".format(system_id,product_id)):
        if(row[1] == product_id and row[3] == system_id):
            n = True
    if n == False:
        sql = "INSERT INTO Subsystems_t VALUES (NULL,'{0}','{1}','{3}') ".format(product_id, product_sum, system_id)
        cursor.execute(sql)
        print("Added subsystem: " + system_name + ": "+product_name+"="+str(product_sum))
        conn.commit()
        return 1
    else:
        print("Subsystem already exists")
        current_sum  = getProductSUM(product_id)
        sql = "UPDATE Subsystems_t SET sum = '{0}' WHERE product_id = '{1}'".format((product_sum+current_sum), product_id)
        cursor.execute(sql)
        conn.commit()
        return 0





if __name__ == "__main__":
    addSubsystem("test_system","test_product",5);