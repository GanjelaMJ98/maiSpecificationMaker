# -*- coding: utf8 -*-
import sqlite3

conn = sqlite3.connect("D:\Code\Git\maiSpecificationMaker\Specifications.sqlite")
cursor = conn.cursor()



cursor.execute("""CREATE TABLE `Products_t` (
    `id`            INTEGER PRIMARY KEY AUTOINCREMENT,
	`product_name`	TEXT,
	`price`	        INTEGER,
	`number`	    INTEGER,
	`contractor`	TEXT,
	`fabricator`	TEXT,
	`currency`	    TEXT,
	`delivery`	    TEXT
)""")

cursor.execute("""CREATE TABLE `Projects_t` (
    `id`	        INTEGER PRIMARY KEY AUTOINCREMENT,
	`project_name`	TEXT
)""")

cursor.execute("""CREATE TABLE `Systems_t` (
    `id`	        INTEGER PRIMARY KEY AUTOINCREMENT,
	`system_name`	TEXT,
	`project_id`	INTEGER,
	FOREIGN KEY(`project_id`) REFERENCES `projects`(`id`)
)""")


cursor.execute("""CREATE TABLE `Subsystems_t` (
    `id`	        INTEGER PRIMARY KEY AUTOINCREMENT,
	`product_id`	INTEGER,
	`sum`	        INTEGER,
	`system_id`	    INTEGER,
	FOREIGN KEY(`product_id`) REFERENCES `Products_t`(`id`),
	FOREIGN KEY(`system_id`) REFERENCES `Systems_t`(`id`)
)""")

#test value
cursor.execute("INSERT INTO Projects_t VALUES (NULL,'test_project_1') ")
cursor.execute("INSERT INTO Projects_t VALUES (NULL,'test_project_2') ")
cursor.execute("INSERT INTO Projects_t VALUES (NULL,'test_project_3') ")
cursor.execute("INSERT INTO Systems_t VALUES (NULL,'test_system_1','1')")
cursor.execute("INSERT INTO Systems_t VALUES (NULL,'test_system_2','2')")
cursor.execute("INSERT INTO Systems_t VALUES (NULL,'test_system_3','1')")
cursor.execute("INSERT INTO Systems_t VALUES (NULL,'test_system_4','2')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'test_product_1','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'test_product_2','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'test_product_3','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'test_product_4','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'test_product_5','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'test_product_6','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'test_product_7','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'1','5','1')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'2','6','2')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'3','4','2')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'4','3','1')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'5','1','4')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'6','1','3')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'7','1','4')")


conn.commit()
conn.close()