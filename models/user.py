#!/usr/bin/python3
"""
This creates a User class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class represents a user in the system.
    Attributes
    ----------
    email : str
        The email address.
    password : str
        The password.
    first_name : str
        The first name.
    last_name : str
        The last name.
    """
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
