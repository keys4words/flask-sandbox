from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login = LoginManager()
login.login_view = "routes.login"


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.BaseConfig')
    db.init_app(app)
    login.init_app(app)

    with app.app_context():
        from views import routes
        app.register_blueprint(routes)
        db.create_all()
        return app
   