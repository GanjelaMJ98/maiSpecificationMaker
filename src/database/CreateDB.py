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
cursor.execute("INSERT INTO Projects_t VALUES (NULL,'Самолёт') ")
cursor.execute("INSERT INTO Projects_t VALUES (NULL,'Автомобиль') ")
cursor.execute("INSERT INTO Projects_t VALUES (NULL,'Дом') ")
cursor.execute("INSERT INTO Projects_t VALUES (NULL,'Мотоцикл') ")
cursor.execute("INSERT INTO Projects_t VALUES (NULL,'Станок') ")
cursor.execute("INSERT INTO Projects_t VALUES (NULL,'Холодильник') ")
cursor.execute("INSERT INTO Systems_t VALUES (NULL,'Фюзеляж','1')")
cursor.execute("INSERT INTO Systems_t VALUES (NULL,'Крыло','1')")
cursor.execute("INSERT INTO Systems_t VALUES (NULL,'Шаси','1')")
cursor.execute("INSERT INTO Systems_t VALUES (NULL,'Система управления','1')")
cursor.execute("INSERT INTO Systems_t VALUES (NULL,'Силовая установка','1')")
cursor.execute("INSERT INTO Systems_t VALUES (NULL,'Бортовое оборудование','1')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'Кабина','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'Топливный бак','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'Багажный отсек','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'Кресло','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'Полка','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'Багажный отсек','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Products_t VALUES (NULL,'Крепление','100','10','t_contr','t_fab','t_cur','t_del')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'1','5','1')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'2','6','1')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'3','4','1')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'4','3','1')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'5','1','1')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'6','1','1')")
cursor.execute("INSERT INTO Subsystems_t VALUES (NULL,'7','1','1')")


conn.commit()
conn.close()