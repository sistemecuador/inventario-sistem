import datetime
from decimal import Decimal

from flask_login import current_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import class_mapper, ColumnProperty

from config.db import db


class AbstractUser:
    """
    This provides default implementations for the methods that Flask-Login
    expects user objects to have.
    """

    # Python 3 implicitly set __hash__ to None if we override __eq__
    # We set it back to its default implementation
    __hash__ = object.__hash__

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return self.is_active

    @property
    def is_anonymous(self):
        return False

    @property
    def is_superuser(self):
        return True

    def get_id(self):
        try:
            return str(self.id)
        except AttributeError:
            raise NotImplementedError("No `id` attribute - override `get_id`") from None

    def __eq__(self, other):
        """
        Checks the equality of two `UserMixin` objects using `get_id`.
        """
        if isinstance(other, AbstractUser):
            return self.get_id() == other.get_id()
        return NotImplemented

    def __ne__(self, other):
        """
        Checks the inequality of two `UserMixin` objects using `get_id`.
        """
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal


class AnonymousUserMixin:
    """
    This is the default object for representing an anonymous user.
    """

    @property
    def is_authenticated(self):
        return False

    @property
    def is_active(self):
        return False

    @property
    def is_anonymous(self):
        return True

    def get_id(self):
        return


class BaseModelMixin:
    date_create = db.Column(db.DateTime, index=True, default=datetime.datetime.now())

    date_update = db.Column(db.DateTime, index=True, default=None)

    def save(self, **kwargs):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print("Error basemodel", str(e))
            raise Exception(str(e))

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            error = str(e)
            print("erro desde delete", error)
            raise Exception(error)

    @classmethod
    def get_all(cls):
        return cls.query.all()
