#!/usr/bin/python3

"""
This file is used to define the storage
of the project AirBnB.
"""

import json
from json.decoder import JSONDecodeError
from datetime import datetime


class FileStorage:
    """
    This is  the fileStorage    like a database for our PrOJECT
    """

    __objects: dict = {}
    __file_path: str = 'file.json'

    def __init__(self):
        """Initializer"""
        pass

    def all(self):
        """displays the stored data"""
        return FileStorage.__objects

    def new(self, obj):
        """add a new instance to the store"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialization conversion and storage"""
        to_ser = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(to_ser, file)

    def reload(self):
        """Deserialization and storage"""
        try:
            to_deser = {}
            with open(FileStorage.__file_path, "r") as file:
                to_deser = json.loads(file.read())
            FileStorage.__objects = {
                k:
                    eval(obj["__class__"])(**obj)
                    for k, obj in to_deser.items()}
        except (FileNotFoundError, JSONDecodeError):
            pass
