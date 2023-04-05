import sqlite3
import random

def primary_key_generator(count):
    return random.sample(range(1, 1000), count)

def main():

    # creating a connection to the database named test.db
    transaction_db = sqlite3.connect('data.db')
    # creation of sample data
    for id in primary_key_generator(10):
        amount = random.randint(1, 1000) * 100
        transaction_db.execute("INSERT INTO TRANSACTIONS (ID) VALUES (id)")
        
        
main()