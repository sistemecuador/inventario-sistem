from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from base.contrib.models import BaseUserModelMixin
from config.db import db


class User(BaseUserModelMixin, db.Model):
    is_admin = db.Column(db.Boolean, default=False)
    is_superuser = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, username, password, first_name=None, last_name=None, is_admin=False, is_superuser=False,
                 is_active=True, correo='sininfo@gmail.com'):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.correo = correo
        self.is_admin = is_admin
        self.is_superuser = is_superuser
        self.is_active = is_active

    def __repr__(self):
        return f'{self.username}'

    @classmethod
    def set_password(self, password):
        pw = generate_password_hash(password)
        return pw

    @classmethod
    def check_password(self, hash_pw, password):
        pw = check_password_hash(hash_pw, password)
        return pw
