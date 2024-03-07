#!/usr/bin/python3
"""
Defines a BaseModel class which is a Base for all classes
"""
import datetime
from uuid import uuid4


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self):
        """
        initiialise instance attributes

        Returns:
            None
        """
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Defines the string representation of the class

        Returns:
            str: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """
        Updates the updateted_at attribute to the current time

        Returns:
            None
        """
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """
        Returns a dictionary containing all the key/value
        pairs of an instance
        Sets the key __clas__ to the name of the class

        Returns:
            dict: dictionary containing key/value pairs of the instance
        """
        self.__dict__["__class__"] = self.__class__.__name__
        new_dict = self.__dict__.copy()
        return new_dict
