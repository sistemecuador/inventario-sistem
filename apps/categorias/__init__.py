from flask import Blueprint

categorias = Blueprint('categorias', __name__, template_folder='static')

from . import routes
