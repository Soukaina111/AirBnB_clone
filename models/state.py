#!/usr/bin/python3
"""
This creates a User class
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state.
    Attributes:
        name (str): The state name.
    """
    name: str = ''
