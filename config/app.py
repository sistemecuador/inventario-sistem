from flask import Flask

from apps.categorias import categorias
from apps.home import home
from apps.login import login
from apps.users import users
from config.constantes import BASE_STATIC_ROOT, BASE_TEMPLATE_ROOT
from config.db import db
from config.settings import config


def create_app():
    app = Flask(__name__, static_folder=BASE_STATIC_ROOT, template_folder=BASE_TEMPLATE_ROOT)
    app.config.from_object(config['developer'])
    db.init_app(app)
    app.register_blueprint(users)
    app.register_blueprint(login)
    app.register_blueprint(home)
    app.register_blueprint(categorias)
    return app
