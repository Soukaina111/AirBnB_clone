#!/usr/bin/python3
"""The base model"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    A base model class that defines common attributes and methods for other classes.

    Public Instance Attributes:
        id (str): Unique identifier assigned to the instance.
        created_at (datetime): Date and time when the instance was created.
        updated_at (datetime): Date and time when the instance was last updated.

    Public Instance Methods:
        __str__(): Returns a string representation of the object.
        save(): Updates the `updated_at` attribute with the current datetime.
        to_dict(): Converts the object to a dictionary representation.

    """
    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime and saves the instance to the storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        If kwargs is not empty, the instance is created using the provided dictionary representation.
        Otherwise, a new instance is created with a unique id and the current datetime.

        Args:
            *args: Unused positional arguments.
            **kwargs: Keyword arguments representing the dictionary representation of the instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        
        if not kwargs:
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string representation of the object in the format:
                "[<class name>] (<id>) <__dict__>"
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the object to a dictionary representation.

        Returns:
            dict: A dictionary containing all keys and values of the object's attributes.
                The dictionary includes an additional key "__class__" with the class name of the object.
                The "created_at" and "updated_at" attributes are converted to string objects in ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
