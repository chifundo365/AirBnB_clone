#!/usr/bin/python3
"""
Unnittest for BaseModel class
"""
import unittest
from datetime import datetime
from uuid import uuid4
import os
import time
import json
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """
    Defines different test case for the BaseModel class's
    attributes and methods
    """
    @classmethod
    def setUp(self):
        """
        Sets up BaseModel instance which will be used in the tests methods
        """
        self.base = BaseModel()

    def test__init__(self):
        """
        Test cases for  the __init__ method.
        Test all the instance attributes
        """
        # test Basemodel id
        self.assertNotEqual(self.base, BaseModel())
        self.assertNotEqual(self.base.id, BaseModel().id)
        self.assertEqual(len(self.base.id), len(str(uuid4())))
        self.assertIsInstance(self.base.id, str)

        # test the created_at
        today = datetime.now()
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertEqual(self.base.created_at.minute, today.minute)
        self.assertEqual(self.base.created_at.month,
                         today.month)
        self.assertEqual(self.base.created_at.day,
                         today.day)
        self.assertEqual(self.base.created_at.second,
                         today.second)
        self.assertLessEqual(self.base.created_at,
                             self.base.updated_at)

        # test the updated_at atrribute
        self.assertIsInstance(self.base.updated_at, datetime)
        self.assertEqual(self.base.updated_at.minute,
                         today.minute)
        self.assertEqual(self.base.updated_at.month,
                         today.month)
        self.assertEqual(self.base.updated_at.day,
                         today.day)
        self.assertEqual(self.base.updated_at.second,
                         today.second)
        # test **kwargs
        dict_obj = self.base.to_dict()
        dict_obj["country"] = "USA"
        new_instance = BaseModel(**dict_obj)
        self.assertIsInstance(new_instance, BaseModel)
        # test created at, updated_at data types
        self.assertIsInstance(new_instance.created_at, datetime)
        self.assertIsInstance(new_instance.updated_at, datetime)
        self.assertIsInstance(new_instance.id, str)
        # check if attributes matches with the values in \ **kwargs
        self.assertEqual(new_instance.created_at, datetime.fromisoformat(
            dict_obj.get("created_at")))
        self.assertEqual(new_instance.updated_at, datetime.fromisoformat(
            dict_obj.get("updated_at")))
        self.assertEqual(dict_obj.get("id"), new_instance.id)
        self.assertEqual(str(new_instance), "[BaseModel] ({}) {}".format(
            new_instance.id,
            new_instance.__dict__
        ))
        self.assertEqual(new_instance.country, "USA")

    def test__str__(self):
        """
        Tests for the string representation of the class
        """
        self.assertEqual(str(self.base), "[BaseModel] ({}) {}".format(
            self.base.id,
            self.base.__dict__
        ))
        self.assertIsInstance(str(self.base), str)

    def test_save(self):
        """
        Test cases for the save method of the BaseModel
        """
        old_date_time = self.base.updated_at
        self.base.save()
        self.assertNotEqual(self.base.updated_at.isoformat,
                            old_date_time.isoformat())
        self.assertIsInstance(self.base.updated_at, datetime)
        self.assertIsNot(self.base.updated_at, old_date_time)

    def test_to_dict(self):
        """
        tests for the BaseModel class's to_dict method
        """
        obj_dict = self.base.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn("__class__", obj_dict)

        # Test if the to dict method returns a dictionary with all attributes
        self.assertIn("id", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)
        self.assertEqual(obj_dict.get("__class__"),
                         self.base.__class__.__name__)

        # tests instance attribute types
        self.assertIsInstance(obj_dict.get("created_at"), str)
        self.assertIsInstance(obj_dict.get("updated_at"), str)
        self.assertIsInstance(obj_dict.get("id"), str)

        # Create new timedate object and compare with the instance.
        self.assertEqual(self.base.created_at, datetime.fromisoformat(
            obj_dict.get("created_at")))
        self.assertEqual(self.base.updated_at, datetime.fromisoformat(
            obj_dict.get("updated_at")))


class Test_BaseModel_save(unittest.TestCase):
    """Test class for the save method of BaseModel with storage engine"""
    @classmethod
    def setUp(self):
        if os.path.isfile("file.json"):
            os.remove("file.json")

    @classmethod
    def tearDown(self):
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def test_one_save(self):
        """tests save method when called one time"""
        bm = BaseModel()
        bm.email = "success@gmail.com"
        old_update_at = bm.updated_at
        old_created_at = bm.created_at
        time.sleep(1)
        bm.save()
        self.assertLess(old_update_at, bm.updated_at)
        self.assertEqual(old_created_at, bm.created_at)

    def test_two_saves(self):
        bm = BaseModel()
        bm.save()
        first_updated_at = bm.updated_at
        time.sleep(2)
        bm.save()
        second_update_at = bm.updated_at
        self.assertGreater(second_update_at, first_updated_at)

    def test_one_file_json(self):
        bm = BaseModel()
        bm.save()
        id = bm.id
        with open("file.json", "r") as file:
            self.assertIn(id, file.read())

    def test_two_file_json(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        bm1_id = bm1.id
        bm2_id = bm2.id
        bm1.save()
        time.sleep(1)
        bm2.save()
        self.assertNotEqual(bm1_id, bm2_id)
        with open("file.json", "r") as file:
            json_str = file.read()
            self.assertIn(bm1_id, json_str)
            self.assertIn(bm2_id, json_str)

    def test_create_one_object(self):
        bm = BaseModel()
        bm.save()
        with open("file.json", "r") as file:
            obj = json.loads(file.read())
            if len(obj) > 1:
                bm_id = bm.id
                for k, v in obj.items():
                    if bm_id in k:
                        obj = obj[k]
            bm_new = BaseModel(**obj)
            self.assertEqual(bm.id, bm_new.id)
            self.assertEqual(bm.created_at, bm_new.created_at)
            self.assertEqual(bm.updated_at, bm_new.updated_at)


if __name__ == "__main__":
    unittest.main()
