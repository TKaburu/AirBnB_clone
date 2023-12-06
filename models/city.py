#!/usr/bin/python3

""" Define the city class """


from models.base_model import BaseModel


class City(BaseModel):
    """
    This is a child class that inherits form BaseModel
    Attribute:
                state id - which is an empty string
                name - which is an empty string
    """

    state_id = ""
    name = ""
