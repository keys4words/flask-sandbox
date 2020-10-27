import sqlite3

connection = sqlite3.connect('my.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    '''DROP TABLE users;
    CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(64),
        position VARCHAR(256)
    );'''
)

connection.commit()
cursor.close()
connection.close()