from flask import Flask
from flaskr import db

app = Flask(__name__)
app.config.from_object('config.DevConfig')
db.init_app(app)

from flaskr import auth, blog

app.register_blueprint(auth.bp)
app.register_blueprint(blog.bp)