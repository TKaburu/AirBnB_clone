#!/usr/bin/python3
"""
BaseModel is the superclass
"""


from datetime import datetime
import uuid


class BaseModel:
    """
    Superclass defines all shared attributes
    """
    def __init__(self, *args, **kwargs):
        """
        instatiates attributes using args and kwargs
        """
        if kwargs:
            # Iterate over the key-value pairs in kwargs
            for key, value in kwargs.items():
                if key == '__class__':
                    continue  # Skip the __class__ key
                if key == 'created_at' or key == 'updated_at':
                    # Convert the string value to a datetime object
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from models.engine.file_storage import storage
            storage.new(self)

    def save(self):
        """
        updates time when object is changes
        """
        self.updated_at = datetime.now()
        from models.engine.file_storage import storage
        storage.save()

    def __str__(self):
        """
        returns a customzed dict string
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        returns a dict represantion of an obj
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
