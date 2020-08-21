from user import User

users = [
    User(1, 'John Dow', 'mypass'),
    User(2, 'Mike Tyson', 'secret'),
]

username_table = {el.username: el for el in users}
userid_table = {el.id: el for el in users}

def authenticate(username, password):
    user = username_table.get(username)
    if user and password == user.password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
