#!/usr/bin/python3

"""
This file is used to define the storage of 
the project AirBnB.
"""

import json
from json.decoder import JSONDecodeError
from models.engine.errors import *
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class FileStorage:
    """
    This is  the fileStorage    like a database for our PrOJECT
    """

    __objects: dict = {}
    __file_path: str = 'file.json'
    models = (
            "BaseModel",
            "User", "City", "State", "Place",
            "Amenity", "Review"
            )

    def __init__(self):
        """Initializer"""
        pass

    def all(self):
        """displays the stored data"""
        return FileStorage.__objects

    def new(self, obje):
        """add a new instance to the store"""
        key = "{}.{}".format(type(obje).__name__, obje.id)
        FileStorage.__objects[key] = obje

    

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


    def search_id(self, mdl, object_id):
        """search an instance using the id  we passed as an argument"""
        FS = FileStorage
        if mdl not in FS.models:
            raise ModelNotFoundError(mdl)
        key = mdl + "." + object_id
        if key not in FS.__objects:
            raise InstanceNotFoundError(object_id, mdl)

        return FS.__objects[key]


    def destroy_id(self, entity, obj_id):
        """destroys an instance using the id  we pass as an argument"""
        FS = FileStorage
        if entity not in FS.models:
            raise ModelNotFoundError(entity)

        k = entity + "." + obj_id
        if k not in FS.__objects:
            raise InstanceNotFoundError(obj_id, entity)

        del FS.__objects[k]
        self.save()


    def retrieve_data(self, entity=""):
        """Retrieves all object of an entity"""
        if entity and entity not in FileStorage.models:
            raise ModelNotFoundError(entity)
        outcome = []
        for key, val in FileStorage.__objects.items():
            if key.startswith(entity):
                outcome.append(str(val))
        return outcome

    def single_modif(self, entity, UI, domain, val):
        """Updates an instance"""
        FS = FileStorage
        if entity not in FS.models:
            raise ModelNotFoundError(entity)

        key = entity + "." + UI
        if key not in FS.__objects:
            raise InstanceNotFoundError(UI, entity)
        if domain in ("id", "updated_at", "created_at"):
            return
        obj = FS.__objects[key]
        try:
            o1 = type(obj.__dict__[domain])
            obj.__dict__[domain] = o1(val)
        except KeyError:
            obj.__dict__[domain] = val
        finally:
            obj.updated_at = datetime.utcnow()
            self.save()

