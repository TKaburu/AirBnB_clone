#!/usr/bin/python3
"""
user class
"""


from models.base_model import BaseModel
import json


class User(BaseModel):
    '''base model class with public attributes'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
