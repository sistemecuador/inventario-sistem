from flask import Blueprint

users = Blueprint('users', __name__, template_folder='templates', static_folder='static',url_prefix='/usuarios')

from . import routes
