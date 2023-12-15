#!/usr/bin/python3
"""tsts places"""
import unittest
import os
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """tests attributes"""

    @classmethod
    def setUpClass(cls):
        """sets up an instance"""
        cls.place1 = Place()
        cls.place1.city_id = "Malindi"
        cls.place1.user_id = "Mine"
        cls.place1.name = "Summer Villa"
        cls.place1.description = "Home away from Home"
        cls.place1.number_rooms = 0
        cls.place1.number_bathrooms = 0
        cls.place1.max_guest = 0
        cls.place1.price_by_night = 0
        cls.place1.latitude = 0.0
        cls.place1.longitude = 0.0
        cls.place1.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """deletes an instance"""
        del cls.place1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """checks if place is a subclass"""
        self.assertTrue(issubclass(self.place1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """checks if doc exists"""
        self.assertIsNotNone(Place.__doc__)

    def test_has_attributes(self):
        """cheks if attributes exists"""
        self.assertTrue('id' in self.place1.__dict__)
        self.assertTrue('created_at' in self.place1.__dict__)
        self.assertTrue('updated_at' in self.place1.__dict__)
        self.assertTrue('city_id' in self.place1.__dict__)
        self.assertTrue('user_id' in self.place1.__dict__)
        self.assertTrue('name' in self.place1.__dict__)
        self.assertTrue('description' in self.place1.__dict__)
        self.assertTrue('number_rooms' in self.place1.__dict__)
        self.assertTrue('number_bathrooms' in self.place1.__dict__)
        self.assertTrue('max_guest' in self.place1.__dict__)
        self.assertTrue('price_by_night' in self.place1.__dict__)
        self.assertTrue('latitude' in self.place1.__dict__)
        self.assertTrue('longitude' in self.place1.__dict__)
        self.assertTrue('amenity_ids' in self.place1.__dict__)

    def test_attributes_are_strings(self):
        """checks if atts are strings and ints"""
        self.assertEqual(type(self.place1.city_id), str)
        self.assertEqual(type(self.place1.user_id), str)
        self.assertEqual(type(self.place1.name), str)
        self.assertEqual(type(self.place1.description), str)
        self.assertEqual(type(self.place1.number_rooms), int)
        self.assertEqual(type(self.place1.number_bathrooms), int)
        self.assertEqual(type(self.place1.max_guest), int)
        self.assertEqual(type(self.place1.price_by_night), int)
        self.assertEqual(type(self.place1.latitude), float)
        self.assertEqual(type(self.place1.longitude), float)
        self.assertEqual(type(self.place1.amenity_ids), list)

    def test_save(self):
        """checks if save updates updated_at"""
        self.place1.save()
        self.assertNotEqual(self.place1.created_at, self.place1.updated_at)

    def test_to_dict(self):
        """checks if to_dict exists"""
        self.assertEqual('to_dict' in dir(self.place1), True)


if __name__ == "__main__":
    unittest.main()
