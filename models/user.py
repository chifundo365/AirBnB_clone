#!/usr/bin/python3
"""
Defines a class user that inherits from BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """Implements a User class derived from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
