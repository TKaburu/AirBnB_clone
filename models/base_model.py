#!/usr/bin/python3

""" Define parent class BaseModel """


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Initialize parent classs
    """
    def __init__(self, *args, **kwargs):

        if kwargs:# if kwargs is not empty
            for key, value in kwargs.items():
                #don't do anything for __class__
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

            #import storage here to avoid circular import error
            from models.engine.file_storage import storage
            models.storage.new(self)

    def __str__(self):
        """
        This public method prints class name, id and dict
        """
        return f"[{self.__class__.__name__}], ({self.id}), {self.__dict__}"

    def save(self):
        """
        This public method updates update_at with current date and time
        """
        self.updated_at = datetime.now()

        #import storage here to avoid circular import error
        from models.engine.file_storage import storage
        models.storage.save()

    def to_dict(self):
        """
        This public method returns a dictionary containing key/ values
        """
        dict_cpy = self.__dict__.copy()
        dict_cpy["__class__"] = self.__class__.__name__
        dict_cpy["created_at"] = self.created_at.isoformat()
        dict_cpy["updated_at"] = self.updated_at.isoformat()
        #dict_cpy["__class__"] = self.__class__.__name__

        return dict_cpy
