import sqlite3

def show_position(username):
    connection = sqlite3.connect('my.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT position FROM users where username='{username}';""".format(username=username))

    positions = cursor.fetchone()

    connection.commit()
    cursor.close()
    connection.close()
    message = f"{username}'s position is {positions}'"
    return message

print(show_position)