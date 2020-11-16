from collections import namedtuple

from flask import Flask, url_for, render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Message = namedtuple('Message', 'text tag')
# messages = []

##################################

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)

    def __init__(self, text, tags):
        self.text = text.strip()
        self.tags = [Tag(text=tag.strip()) for tag in tags.split(',')]


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), nullable=False)
    
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', backref=db.backref('tags', lazy=True))

db.create_all()

###################################

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/main')
def main():
    return render_template('main.html', messages=Message.query.all())


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    # messages.append(Message(text, tag))
    db.session.add(Message(text, tag))
    db.session.commit()
    return redirect(url_for('main'))



if __name__ == "__main__":
    app.run(debug=True)