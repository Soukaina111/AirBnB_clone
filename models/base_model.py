#!/usr/bin/python3
"""this is the base model class """
from models import storage
import uuid
from datetime import datetime


class BaseModel:
    """
    A base class that defines commo
    attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.

        Args:
            *args: Not used.
            **kwargs: A dictionary containing attribute
            names and their corresponding values.
        If kwargs is not empty:
            - Each key of this dictionary is an attribute name.
            - Each value of this dictionary is the value of the
            attribute name.
            - The 'created_at' and 'updated_at' attributes are
             converted from strings to datetime objects.
        If kwargs is empty:
            - The id and created_at attributes are
            created as in the previous implementation.
        """
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string representation in
            the format [<class name>] (<id>) <__dict__>.
        """
        cls = self.__class__.__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.

        Returns:
            dict: A dictionary containing all keys/values of
            __dict__ of the instance.
                  The dictionary includes the __class__ key
                  with the class name and converts the created_at
                  and updated_at attributes to
                  ISO format (%Y-%m-%dT%H:%M:%S.%f).
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
