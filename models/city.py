#!/usr/bin/python3
"""
This creates a User class.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city.
    Attributes:
        state_id (str): The state ID.
        name (str): The city name.
    """
    state_id: str = ''
    name: str = ''
