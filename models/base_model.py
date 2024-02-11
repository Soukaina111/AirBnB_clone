#!/usr/bin/python3
import uuid
from datetime import datetime
from models.engine.file_storage import storage



class BaseModel:
    """
    Base class for other models.
    
    Public instance attributes:
        id (str): Unique identifier assigned to each instance.
        created_at (datetime): Datetime when an instance is created.
        updated_at (datetime): Datetime when an instance is created or last updated.
    
    Public instance methods:
        save(): Updates the `updated_at` attribute with the current datetime.
        to_dict(): Returns a dictionary representation of the instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.
        
        Args:
            *args: Variable length argument list. Not used in this implementation.
            **kwargs: Arbitrary keyword arguments. If not empty, each key-value pair represents an attribute.
                      The '__class__' key is ignored, and the 'created_at' and 'updated_at' strings are converted
                      to datetime objects.
        """
        self.id = str(uuid.uuid4())  # Assign a unique id to each instance
        self.created_at = datetime.now()  # Assign the current datetime when an instance is created
        self.updated_at = self.created_at  # Initialize updated_at with the creation datetime

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()  # Update updated_at with the current datetime

    def to_dict(self):
        """
        Return a dictionary representation of the instance.

        Returns:
            dict: Dictionary containing all keys and values of the instance.
                The dictionary includes a '__class__' key with the class name,
                and the 'created_at' and 'updated_at' attributes are converted to ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__  # Add the class name to the dictionary
        obj_dict['created_at'] = self.created_at.isoformat()  # Convert created_at to ISO format
        obj_dict['updated_at'] = self.updated_at.isoformat()  # Convert updated_at to ISO format
        return obj_dict
    
    def save(self):
        """Save the instance and call the save() method of storage."""
        self.updated_at = datetime.now()
        storage.save()

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)

        storage.new(self)
