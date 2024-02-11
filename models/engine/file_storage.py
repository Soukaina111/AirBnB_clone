#!/usr/bin/python3
"""The FileStorage"""

import json
from os.path import exists
from models.user import User
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON files to instances.

    Private Class Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store all objects by <class name>.id.

    Public Instance Methods:
        all(self): Returns the dictionary __objects.
        new(self, obj): Sets the obj with the key <obj class name>.id in __objects.
        save(self): Serializes __objects to the JSON file.
        reload(self): Deserializes the JSON file to __objects.
    """

    __file_path = "file.json"
    __objects = {}


    CLASSES = {
        "BaseModel": BaseModel,
        "User": User
        # Add other classes here if needed
    }

    def all(self):
        """
        Returns the dictionary __objects.

        Returns:
            dict: The dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets the obj with the key <obj class name>.id in __objects.

        Args:
            obj (BaseModel): The object to be added to __objects.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)

            for key, obj_data in obj_dict.items():
                class_name, obj_id = key.split('.')
                class_module = __import__("models.{}".format(class_name), fromlist=[class_name])
                class_ = getattr(class_module, class_name)
                obj = class_(**obj_data)
                self.__objects[key] = obj


