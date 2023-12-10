#!/usr/bin/python3

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """tests for attributes in amenity"""

    @classmethod
    def setUpClass(cls):
        """sets up an instance"""
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Hot Tub"

    @classmethod
    def tearDownClass(cls):
        """delete an instance"""
        del cls.amenity1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """checks if a subclass"""
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """checks id doc is present"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        """checks if atts are available"""
        self.assertTrue('id' in self.amenity1.__dict__)
        self.assertTrue('created_at' in self.amenity1.__dict__)
        self.assertTrue('updated_at' in self.amenity1.__dict__)
        self.assertTrue('name' in self.amenity1.__dict__)

    def test_attributes_are_strings(self):
        """checks if atts is a str"""
        self.assertEqual(type(self.amenity1.name), str)

    def test_save(self):
        """check if save updates updated_at"""
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_to_dict(self):
        """checks if to_dict is available"""
        self.assertEqual('to_dict' in dir(self.amenity1), True)


if __name__ == "__main__":
    unittest.main()
