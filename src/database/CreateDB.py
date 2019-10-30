import sqlite3
conn = sqlite3.connect('./Specifications.sqlite')
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


cursor.execute("""CREATE TABLE `Subystem_t` (
    `id`	        INTEGER PRIMARY KEY AUTOINCREMENT,
	`product_id`	TEXT,
	`sum`	        INTEGER,
	`system_id`	    INTEGER,
	FOREIGN KEY(`product_id`) REFERENCES `Products_t`(`id`),
	FOREIGN KEY(`system_id`) REFERENCES `Systems_t`(`id`)
)""")



conn.close()