#!/usr/bin/python3

"""
This file defines  the BaseModel class
that defines all common attributes/methods
for other classes
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """ Constructor of the  class  """

        """Initialize the attributes if no arguments was passed"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            return

        if 'id' not in kwargs:
            kwargs['id'] = str(uuid4())
        self.id = kwargs['id']

        for K, v in kwargs.items():
            if K == "__class_":
                continue
        if "created_at" in kwargs:
            self.created_at = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """new str representation of self"""
        newrep = "[{}] ({}) {}"
        return newrep.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """stores the updated attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """displays the dictionary representation of self"""
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dict['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return dict

    def update(cls, att_id, *args):
            """Updates an instance considering multiple cases"""
            if len(args) == 0:
                  print("** attribute name missing **")
                  return
            if len(args) == 1 and isinstance(args[0], dict):
                  for key, value in args[0].items():
                        models.storage.single_modif(cls.__name__, att_id, key, value)
            else:
                  if len(args) >= 2:
                        models.storage.single_modif(cls.__name__, att_id, args[0], args[1])
