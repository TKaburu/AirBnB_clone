#!/usr/bin/python3
"""tests on user class"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """tests attributes"""

    @classmethod
    def setUpClass(cls):
        """sets up an instance"""
        cls.my_user = User()
        cls.my_user.first_name = "Betty"
        cls.my_user.last_name = "Alx"
        cls.my_user.email = "airbnb@alx.com"
        cls.my_user.password = "root"

    @classmethod
    def tearDownClass(cls):
        """deletes an instance"""
        del cls.my_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """tests if user is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """checks for methods in user"""
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        """checks for attributes in user"""
        self.assertTrue('email' in self.my_user.__dict__)
        self.assertTrue('id' in self.my_user.__dict__)
        self.assertTrue('created_at' in self.my_user.__dict__)
        self.assertTrue('updated_at' in self.my_user.__dict__)
        self.assertTrue('password' in self.my_user.__dict__)
        self.assertTrue('first_name' in self.my_user.__dict__)
        self.assertTrue('last_name' in self.my_user.__dict__)

    def test_attributes_are_strings(self):
        """checks if attributes are strings"""
        self.assertEqual(type(self.my_user.email), str)
        self.assertEqual(type(self.my_user.password), str)
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.first_name), str)

    def test_save(self):
        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def test_to_dict(self):
        """checks if to_dict is available to user"""
        self.assertEqual('to_dict' in dir(self.my_user), True)


if __name__ == "__main__":
    unittest.main()
