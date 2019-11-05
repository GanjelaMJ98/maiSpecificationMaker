# -*- coding: utf8 -*-
import sqlite3
import os.path
BASE_DIR = os.path.dirname(os.path.abspath(".."))

db_path = os.path.join(BASE_DIR, "Specifications.sqlite")
conn = sqlite3.connect(db_path)
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
cursor.execute("INSERT INTO Projects_t VALUES (NULL,'test_project') ")
cursor.execute("INSERT INTO Systems_t VALUES (NULL,'test_system','1')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'test_product','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'1','3','1')")
conn.commit()
conn.close()