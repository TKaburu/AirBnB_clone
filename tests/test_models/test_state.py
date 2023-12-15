#!/usr/bin/python3
"""unittests for State class"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """tests on attributes"""

    @classmethod
    def setUpClass(cls):
        """sets up an instance"""
        cls.state1 = State()
        cls.state1.name = "Nairobi"

    @classmethod
    def tearDownClass(cls):
        """deletes instance"""
        del cls.state1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """tests is state is a subclass"""
        self.assertTrue(issubclass(self.state1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """tests if methods are available"""
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        """checks that atts are available"""
        self.assertTrue('id' in self.state1.__dict__)
        self.assertTrue('created_at' in self.state1.__dict__)
        self.assertTrue('updated_at' in self.state1.__dict__)
        self.assertTrue('name' in self.state1.__dict__)

    def test_attributes_are_strings(self):
        """checks that atts are strings"""
        self.assertEqual(type(self.state1.name), str)

    def test_save(self):
        """checks the save method"""
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_to_dict(self):
        """checks if to_dict is available to state"""
        self.assertEqual('to_dict' in dir(self.state1), True)


if __name__ == "__main__":
    unittest.main()
