from config.constantes import UPLOAD_FOLDER


class Config(object):
    DEBUG = False
    # SERVER_NAME = 'localhost:6000'
    SECRET_KEY = 'kjasgsjgsjdgjsdkkjsdjhgsdhgdsjbh'
    UPLOAD_FOLDER = UPLOAD_FOLDER
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = 'app.py'



class Developer(Config):
    SQLALCHEMY_DATABASE_URI = f'postgresql://postgres:Nomeacuerdo123.@localhost:5433/inventario'


class Productions(Config):
    SQLALCHEMY_DATABASE_URI = f'postgresql://postgres:Nomeacuerdo123.@localhost:5433/inventario'


class Test(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'


config = {
    'developer': Developer,
    'productions': Productions,
    'test': Test,
}
