#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
"""
a specified filr for testing the basemodel from which
all models inherent
class
"""


class TestBaseModel(unittest.TestCase):
    """
    testing the efficiency of the basemodel
    """
    def startup(self):
        """
        dealing with prerequisties of testing operation
        """
        pass

    def test_save(self):
        """
        testing the save method of BaseModel
        """
        pass

    def test_to_dict(self):
        """
        testing the to_dict method of BaseModel
        """
        pass

    def teardown(self):
        pass


if __name__ == "__main__":
    unittest.main()
