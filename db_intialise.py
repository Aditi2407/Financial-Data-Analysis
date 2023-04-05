
# importing the sql module
import sqlite3

# creating a connection to the database named test.db
transaction_db = sqlite3.connect('data.db')

# destroys the table if it exists
transaction_db.execute('''DROP TABLE IF EXISTS TEST''')

# creating a cursor to execute the sql commands, SQL commands are parsed a strings enclosed by 3 
transaction_db.execute('''CREATE TABLE IF NOT EXISTS TRANSACTIONS
                      (ID INTEGER PRIMARY KEY ,
                        TIMESTAMP DATE ,
                      AMOUNT INT );''')

transaction_db.execute('''CREATE TABLE IF NOT EXISTS ACCOUNTS
                      (ID INTEGER PRIMARY KEY NOT NULL,
                        PAYEE_ID INT NOT NULL,
                       RECEIVER_ID INT NOT NULL);''')


transaction_db.execute('''CREATE TABLE IF NOT EXISTS STATUS
                      (ID INTEGER PRIMARY KEY NOT NULL,
                        FLAG INT NOT NULL);''')






transaction_db.commit()





transaction_db.commit()
transaction_db.close()