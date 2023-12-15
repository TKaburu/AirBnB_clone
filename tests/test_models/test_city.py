#!/usr/bin/python3
"""unitest for city"""

import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """tests for attributes"""

    @classmethod
    def setUpClass(cls):
        """sets instance"""
        cls.city1 = City()
        cls.city1.name = "Nairobi"
        cls.city1.state_id = "NR"

    @classmethod
    def tearDownClass(cls):
        """delete instance"""
        del cls.city1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """checks if it is a subclass"""
        self.assertTrue(issubclass(self.city1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """checks if doc is available"""
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        """checks if attributes are available"""
        self.assertTrue('id' in self.city1.__dict__)
        self.assertTrue('created_at' in self.city1.__dict__)
        self.assertTrue('updated_at' in self.city1.__dict__)
        self.assertTrue('state_id' in self.city1.__dict__)
        self.assertTrue('name' in self.city1.__dict__)

    def test_attributes_are_strings(self):
        """checks if attributes are strings"""
        self.assertEqual(type(self.city1.name), str)
        self.assertEqual(type(self.city1.state_id), str)

    def test_save(self):
        """checks if it works"""
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_to_dict(self):
        """checks if to_dict exists"""
        self.assertEqual('to_dict' in dir(self.city1), True)


if __name__ == "__main__":
    unittest.main()
