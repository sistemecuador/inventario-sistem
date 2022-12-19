from base.model_mixin.models import BaseModelMixin
from config.db import db


class Categorias(BaseModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(50), unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True)

    def __init__(self, nombre_categoria, activo):
        self.nombre_categoria = nombre_categoria
        self.activo = activo
