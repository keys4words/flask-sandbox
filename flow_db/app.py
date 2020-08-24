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


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    pets = db.relationship('Pet', backref='owner')

    def __repr__(self):
        return f"<Person {self.name}"


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    new_field = db.Column(db.String(60))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))



@app.route('/')
def index():
    nick = Person.query.filter_by(name='Nick Farrel').first()
    return "Hello " + nick.name

# if app.debug:
#     app.after_request(sql_debug)

# def sql_debug(response):
#     queries = list(get_debug_queries())
#     query_str = ''
#     total_duration = 0.0
#     for q in queries:
#         total_duration += q.duration
#         stmt = str(q.statement % q.parameters).replace('\n', '\n       ')
#         query_str += 'Query: {0}\nDuration: {1}ms\n\n'.format(stmt, round(q.duration * 1000, 2))

#     print('=' * 80)
#     print(' SQL Queries - {0} Queries Executed in {1}ms'.format(len(queries), round(total_duration * 1000, 2)))
#     print('=' * 80)
#     print(query_str.rstrip('\n'))
#     print('=' * 80 + '\n')

#     return response

# app.after_request(sql_debug)

if __name__ == "__main__":
    app.run(debug=True)




@app.cli.command("initdb")
def set_db():
    """add data to table"""
    nick = Person(name='Nick Farrel')
    dunkan = Person(name='Dunkan Macclaud')
    jenny = Person(name='Jenny Piers')
    db.session.add(nick)
    db.session.add(dunkan)
    db.session.add(jenny)
    bars = Pet(name='Barsik', owner=nick)
    bobik = Pet(name='Bob', owner=nick)
    twinni = Pet(name='Twinni', owner=jenny)
    db.session.add_all((bars, bobik, twinni))
    db.session.commit()

    print("Data added to DB")

