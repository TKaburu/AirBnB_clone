#!/usr/bin/python3

""" This is the file storage class """


import json
from models.base_model import BaseModel


class FileStorage:
    """
    This class serialises instances to JSON files
    and deserialises JSON files to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This method returns dictionary for the objects
        """
        return self.__objects

    def new(self, obj): 
        """
        This method adds new objects to the dictionary
        Args:
            obj: The new object
        """

        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self): 
        """
        This method serialises instances to JSON files
        """
        object_dict = {}
        for key, obj in self.__objects.items():
            object_dict[key] = obj.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as files:
            json.dump(object_dict, files)

    def reload(self):
        """
        This method deserialises JSON files
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as files:
               object_dict  = json.load(files)
            for key, value in object_dict.items():
                class_name, obj_id = key.split(".")
                self.__objects[key] = globals()[class_name](**value)

        except FileNotFoundError:
            pass

storage = FileStorage()
storage.reload()
