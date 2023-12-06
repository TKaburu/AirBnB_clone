#!/usr/bin/python3

""" Defines the review class """

from models.base_model import BaseModel


class Review(BaseModel):
    """
    This is a child clase that inherites from BaseModel
    Attributes:
                place_id - which is an empty string
                user_id - which is an empty string
                text - which is an empty string
    """

    place_id = ""
    user_id = ""
    text = ""
