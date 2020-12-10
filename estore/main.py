import os

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'shop.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#########################
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    # desc = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Product: {self.title}>'


#########################
@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()

    return render_template('index.html', data=items)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        
        item = Item(title=title, price=price)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return 'Error happens!'
    else:
        return render_template('create.html')


@app.route('/buy/<int:id>')
def item_buy(id):

    return str(id)







##########################

if __name__ == "__main__":
    app.run(debug=True)