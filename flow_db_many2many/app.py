import os
from flask import Flask, render_template, url_for, request, session, redirect, abort, flash
from flask_sqlalchemy import SQLAlchemy, get_debug_queries
from flask_migrate import Migrate

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'flow-db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)



subs = db.Table('subs',
            db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
            db.Column('channel_id', db.Integer, db.ForeignKey('channel.id'))
            )

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    subscriptions = db.relationship('Channel', secondary=subs, backref=db.backref('subscribers', lazy='dynamic'))

    def __repr__(self):
        return f"<User {self.name}>"


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))

    def __repr__(self):
        return f"<Channel {self.name}>"



@app.route('/')
def index():
    channels = Channel.query.all()
    res = ''
    for channel in channels:
        res += channel.name + ' subscribers: {'
        for user in channel.subscribers:
            res += user.name + ', '
        res += '}\n'
    return res

if __name__ == "__main__":
    app.run(debug=True)




@app.cli.command("initdb")
def set_db():
    """add data to table"""
    nick = User(name='Nick Farrel')
    dunkan = User(name='Dunkan Macclaud')
    jenny = User(name='Jenny Piers')
    db.session.add(nick)
    db.session.add(dunkan)
    db.session.add(jenny)
    geo = Channel(name='National Geographic')
    bbc = Channel(name='BBC News')
    rt = Channel(name='Russia Today')
    db.session.add_all((geo, bbc, rt))
    geo.subscribers.extend([nick, dunkan])
    bbc.subscribers.append(nick)
    rt.subscribers.append(jenny)
    db.session.commit()

    print("Data added to DB")

