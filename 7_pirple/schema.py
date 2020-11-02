import sqlite3

connection = sqlite3.connect('my.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    '''CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR(256),
        password VARCHAR(64),
        position VARCHAR(256)
    );'''
)

connection.commit()
cursor.close()
connection.close()