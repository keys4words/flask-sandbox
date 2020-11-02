import sqlite3


connection = sqlite3.connect('my.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""INSERT INTO users(email, password, position) VALUES ('maroon5@yahoo.com', 'songs', 'music')""")
cursor.execute("""INSERT INTO users(email, password, position) VALUES('mike_tyson@yahoo.com', 'box', 'boxer')""")
cursor.execute("""INSERT INTO users(email, password, position) VALUES ('jeremy_hunt@yahoo.com', 'aalsdjf', 'spy')""")

connection.commit()
cursor.close()
connection.close()