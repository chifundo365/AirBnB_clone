#!/usr/bin/python3
"""
Defines a BaseModel class which is a Base for all classes
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        initialise instance attributes
        Returns:
            None
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        dt_format = "%Y-%m-%dT%H:%M:%S.%f"
                        self.__dict__[k] = datetime.strptime(v, dt_format)
                    else:
                        self.__dict__[k] = v
        else:
            models.storage.new(self)

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
        Updates the updateted_at attribute to the current datetime

        Returns:
            None
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all the key/value
        pairs of an instance
        Sets the key __class__ to the name of the class

        Returns:
            dict: dictionary containing key/value pairs of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict.get("created_at").isoformat()
        new_dict["updated_at"] = new_dict.get("updated_at").isoformat()
        return new_dict
