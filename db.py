# importing the sql module
import sqlite3

# creating a connection to the database named test.db
connection_db = sqlite3.connect('test.db')

# destroys the table if it exists
connection_db.execute('''DROP TABLE IF EXISTS TEST''')

# creating a cursor to execute the sql commands, SQL commands are parsed a strings enclosed by 3 
connection_db.execute('''CREATE TABLE TEST
                      (ID INTEGER PRIMARY KEY NOT NULL,
                      NAME TEXT NOT NULL,
                      AGE INT NOT NULL);''')

# inserting values into the table
connection_db.execute("INSERT INTO TEST (ID, NAME, AGE) VALUES (1, 'John', 20)")
connection_db.execute("INSERT INTO TEST (ID, NAME, AGE) VALUES (2, 'John', 30)")
connection_db.execute("INSERT INTO TEST (ID, NAME, AGE) VALUES (3, 'John', 40)")

connection_db.commit()
connection_db.close()