#!/usr/bin/python3
"""The FileStorage"""

import json

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.

        Returns:
            dict: The dictionary containing all objects stored by <class name>.id.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the given object with key <obj class name>.id.

        Args:
            obj: The object to be stored.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file (__file_path) to __objects.
        If the file doesn't exist, does nothing.
        """
        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    module = __import__("models." + class_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    obj = class_(**obj_data)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
