#!/usr/bin/python3

""" Define User class that inherits from BaseModel """


from models.base_model import BaseModel


class User(BaseModel):
    """
    This is a child class that inherits from BaseModel
    Attributes:
                email - which is an empty string
                password - which is an empty string
                first_name - which is an empty string
                last_name - which is an empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
