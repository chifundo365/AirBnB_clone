#!/usr/bin/python3
"""
Unnittest for BaseModel class
"""
import unittest
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel

class Test_BaseModel(unittest.TestCase):
    """
    Defines different test case for the BaseModel class's
    attributes and methods
    """
    def setUp(self):
        self.base = BaseModel()

    def test__init__(self):
        #test the id atrribute
        self.assertNotEqual(self.base, BaseModel())
        self.assertNotEqual(self.base.id, BaseModel().id)
        self.assertEqual(len(self.base.id), len(BaseModel().id))

        #test the created_at
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertEqual(self.base.created_at.minute,
                         BaseModel().created_at.minute)
        self.assertEqual(self.base.created_at.month,
                         BaseModel().created_at.month)
        self.assertEqual(self.base.created_at.day,
                         BaseModel().created_at.day)
    
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()