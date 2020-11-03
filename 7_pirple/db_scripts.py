import sqlite3

connection = sqlite3.connect('my.db', check_same_thread=False)
cursor = connection.cursor()

# create db
# cursor.execute('''CREATE TABLE users(
#         pk INTEGER PRIMARY KEY AUTOINCREMENT,
#         login VARCHAR(256),
#         email VARCHAR(256),
#         password VARCHAR(64));''')

# add data to table
cursor.execute("""INSERT INTO users(login, email, password) VALUES ('Maroon 5', 'maroon5@yahoo.com', 'songs');""")
cursor.execute("""INSERT INTO users(login, email, password) VALUES('Mike Tyson', 'm.tyson@yahoo.com', 'box');""")
cursor.execute("""INSERT INTO users(login, email, password) VALUES ('Jeremy Hunt', 'j_hunt@yahoo.com', 'aalsdjf');""")


connection.commit()
cursor.close()
connection.close()