from base.model_mixin.models import AbstractUser, BaseModelMixin
from config.db import db


class BaseUserModelMixin(AbstractUser, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    correo = db.Column(db.String(200), nullable=True, default='sininfo@gmail.com')
