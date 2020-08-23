import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'flow-db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Example(db.Model):
    __tablename__ = 'example'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(60))

    def __repr__(self):
        return f"<Example with data: {self.data}"


@app.cli.command("initdb")
def set_db():
    """add data to table"""
    db.session.add(Example(data='something new'))
    db.session.add(Example(data='second line'))
    db.session.add(Example(data='third line'))
    db.session.commit()

    print("Data added to DB")

