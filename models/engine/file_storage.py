#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    This class represents a file-based storage system for objects.
    It provides methods for storing, retrieving, and deleting objects in a JSON file.
    """

    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """
        Returns a dictionary containing all objects stored in the storage.
        The keys of the dictionary are in the format '<class name>.<object id>',
        and the values are the actual object instances.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj: The object to be added to the storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects in the storage to a JSON file.
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Reloads objects from the JSON file and populates the storage.
        """
        try:
            with open(self.__file_path, "r") as file:
                serialized_objects = json.load(file)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split(".")
                    cls = self.classes[class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes an object from the storage.

        Args:
            obj: The object to be deleted from the storage.
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """
        Closes the storage and reloads any saved objects.
        """
        self.reload()
