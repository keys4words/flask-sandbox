import sqlite3


connection = sqlite3.connect('my.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(username, password, position)
    VALUES ('Maroon 5', 'songs', 'music')
    """
)

#VALUES('Mike Tyson', 'box', 'boxer')
# VALUES ('Jeremy Hunt', 'aalsdjf', 'spy')
connection.commit()
cursor.close()
connection.close()