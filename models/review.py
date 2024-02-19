#!/usr/bin/python3
"""
This creates a Review class
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review in the application.
    Attributes:
        place_id (str): The place ID.
        user_id (str): The user ID.
        text (str): The review text content.
    """
    place_id: str = ''
    user_id: str = ''
    text: str = ''
