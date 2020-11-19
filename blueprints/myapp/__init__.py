from flask import Flask

from .api.views import api
from .site.views import site
from .admin.views import admin

def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)
    app.register_blueprint(site)
    app.register_blueprint(admin)

    return app

