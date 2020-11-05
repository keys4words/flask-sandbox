from flask import g
import sqlite3

def check_psw(login, psw):
    with sqlite3.connect('my.db', check_same_thread=False) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users where login='{login}';")
        user = cursor.fetchone()
        if user:
            g.user = user[1]
            return psw == user[3]
        return False

def get_user(login):
    with sqlite3.connect('my.db', check_same_thread=False) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users where login='{login}'")
        return cursor.fetchone()

def get_users():
    with sqlite3.connect('my.db', check_same_thread=False) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")
        db_users = cursor.fetchall()

        users = dict()
        for user in db_users:
            users[user[1]] = [user[2], user[3]]
        return users


def signup(login, email, password):
    with sqlite3.connect('my.db', check_same_thread=False) as conn:
        cursor = conn.cursor()
        if get_user(login):
            msg = 'User with this login already exists! Please login!'
        else:
            cursor.execute(f"INSERT INTO users(login, email, password) VALUES('{login}','{email}', '{password}');")
            msg = f'User with login {login} was successfully signup!'
            
        return msg