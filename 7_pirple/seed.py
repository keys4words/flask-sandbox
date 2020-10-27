import sqlite3


connection = sqlite3.connect('my.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    '''INSERT INTO users(username, password, position)
     VALUES('Mike Tyson', 'box', 'boxer'),
    ('Jeremy Hunt', 'aalsdjf', 'spy')
    ('Maroon 5', 'songs', 'music');'''
)

connection.commit()
cursor.close()
connection.close()