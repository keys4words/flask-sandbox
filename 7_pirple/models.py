from runner import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    login = db.Column('login', db.String(100))
    email = db.Column('email', db.String(256))
    password = db.Column('password', db.String(256))
    todos = db.relationship('ToDo', backref='todo', lazy='dynamic')

    def __init__(self, login, email, password):
        self.login = login
        self.email = email
        self.password = password
        
        def __repr__(self):
            return f'<User: {self.login} with email: {self.email}>'


class ToDo(db.Model):
    __tablename__ = 'todo'
    id = db.Column('todo_id', db.Integer, primary_key=True)
    task = db.Column('todo_name', db.Text)
    priority = db.Column('priority', db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, task, priority, user_id):
        self.task = task
        self.priority = priority
        self.user_id = user_id

    def __repr__(self):
        return f'{self.task}'


def seed_db(db):
    james = Users('James Bond', 'j.bond@yahoo.com', 'bond')
    tyson = Users('Mike Tyson', 'boxing@gmail.com', 'boxing')
    data_users = [james, tyson]
    db.session.add_all(data_users)
    db.session.commit()
    
    james_todo1 = ToDo('Sex with blond', 'high', james.id)
    james_todo2 = ToDo('Kill the spy', 'high', james.id)
    tyson_todo1 = ToDo('first round', 'middle', tyson.id)
    tyson_todo2 = ToDo('second round', 'middle', tyson.id)
    tyson_todo3 = ToDo('third round', 'low', tyson.id)
    
    data_todos = [james_todo1, james_todo2, tyson_todo1, tyson_todo2, tyson_todo3]
    db.session.add_all(data_todos)
    db.session.commit()
