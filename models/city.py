#!/usr/bin/python3
"""
Defines a  class representing a city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class derived from BaseModel representing a city"""
    state = ""
    name = ""
