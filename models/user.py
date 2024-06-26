#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
import hashlib
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


def hash_password(password):
    """ Hashing method for password """
    return hashlib.md5(password.encode()).hexdigest()


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.password = hash_password(kwargs['password'])

    @property
    def get_pass(self):
        """ Get password """
        return self.password

    @get_pass.setter
    def get_pass(self, value):
        """Setter for the password attribute that hashes the password."""
        self.password = hash_password(value)
