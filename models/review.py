#!/usr/bin/python3
"""Defines a class representing review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class inheriting from the BaseModel representing review"""
    place_id = ""
    user_id = ""
    text = ""
