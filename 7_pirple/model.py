import sqlite3

def check_psw(login, psw):
    connection = sqlite3.connect('my.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT position FROM users where login='{login}';""".format(login=login))

    user = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    if user:
        return psw == user[2]
    return False

def get_user(login):
    connection = sqlite3.connect('my.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM users where login='{login}';""".format(login=login))
    
    user = cursor.fetchone()

    connection.commit()
    cursor.close()
    connection.close()
    return user

def get_users():
    connection = sqlite3.connect('my.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users;")
    db_users = cursor.fetchall()

    users = dict()
    for user in db_users:
        users[user[1]] = [user[2], user[3]]

    connection.commit()
    cursor.close()
    connection.close()
    
    return users


def signup(login, email, password):
    connection = sqlite3.connect('my.db', check_same_thread=False)
    cursor = connection.cursor()
    no_form = False
    if get_user(login):
        msg = 'User with this login already exists! Please login!'
    else:
        cursor.execute("""INSERT INTO users(login, email, password) VALUES('{login}','{email}', '{password}');""".format(login=login, email=email, password=password))
        msg = f'User with login {login} was successfully signup!'
        
    connection.commit()
    cursor.close()
    connection.close()
    return msg, no_form