#!/usr/bin/python3
"""
This creates a Place class
"""


from models.base_model import BaseModel
from typing import List


class Place(BaseModel):
    """
    Represents a place.
    Attributes:
        city_id (str): The city ID.
        user_id (str): The user ID.
        name (str): The place name.
        description (str): The place description .
        number_rooms (int): The rooms number.
        number_bathrooms (int): The bathrooms number.
        max_guest (int): Max number of guests.
        price_by_night (int): The price per night.
        latitude (float): The latitude coordinate.
        longitude (float): The longitude coordinate.
        amenity_ids (list): The amenity IDs list.
    """
    city_id: str = ''
    user_id: str = ''
    name: str = ''
    description: str = ''
    number_rooms:  int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude:  float = 0.0
    amenity_ids:  List[str] = []
