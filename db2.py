
# importing the sql module
import sqlite3

# creating a connection to the database named test.db
connection_db = sqlite3.connect('test.db')

all_data = connection_db.execute("SELECT * FROM TEST")
#print(all_data)

for row in all_data:
    print(row)


