from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash
from flask_admin.contrib.fileadmin import FileAdmin
from os.path import dirname, join


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
admin = Admin(app, template_mode='bootstrap3')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String(256))
    age = db.Column(db.Integer)
    birthday = db.Column(db.DateTime)
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(200))
    usr_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Comment {self.id}>'

class CommentView(ModelView):
    create_modal = True


class UserView(ModelView):
    # column_exclude_list = ['password']
    column_display_pk = True
    can_create = True
    can_edit = True
    can_delete = False
    can_export = True

    def on_model_change(self, form, model, is_created):
        # model.password = 'you-dont-see-real-password'
        model.password = generate_password_hash(model.password, method='sha256')

    inline_models = [Comment]


class NotificationsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/notification.html')


admin.add_view(UserView(User, db.session))
admin.add_view(CommentView(Comment, db.session))

path = join(dirname(__file__), 'uploads')
admin.add_view(FileAdmin(path, '/uploads/', name='Uploads'))
admin.add_view(NotificationsView(name='Notifications', endpoint='notify'))


if __name__ == "__main__":
    app.run()