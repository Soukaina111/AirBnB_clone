#!/usr/bin/python3
"""
This creates Amenity class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity.
    Attributes:
        name (str): the amenity name.
    """
    name: str = ''
