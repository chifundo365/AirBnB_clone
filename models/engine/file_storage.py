#!/usr/bin/python3
"""
Defines FileStorage class for instance serialization and deserialization
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Implement FileStorage class for serialising and deserialising instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in FIleStorage.___objects the obj
          with the key <class name.id>
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialises __objects to the JSON file"""
        with open(self.__file_path, "w") as file:
            dict_instance = {}
            for k, v in self.__objects.items():
                dict_instance[k] = v.to_dict()
            file.write(json.dumps(dict_instance))

    def reload(self):
        """Deserialises the json file to __objects"""
        from os.path import isfile
        if isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                dict_obj = json.loads(file.read())
                for v in dict_obj.values():
                    o_name = v.get("__class__")
                    del v["__class__"]
                    self.new((eval(o_name)(**v)))
