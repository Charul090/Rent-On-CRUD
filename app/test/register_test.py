import unittest
from ..main.services.owner import register as owner_register


class RegisterTest(unittest.TestCase):

    def test_register_success(self):

        obj = {
            "firstname": "A",
            "lastname": "B",
            "email": "a@gmail.com",
            "password": "A"
        }

        self.assertTrue(owner_register(obj))

    def test_register_error(self):

        obj = {
            "password": "hia"
        }

        self.assertFalse(owner_register(obj))

    def test_register_empty(self):

        obj = {
            "firstname": "A",
            "lastname": "",
            "email": "a@gmail.com",
            "password": "A"
        }

        self.assertFalse(owner_register(obj))

    def test_register_type(self):

        obj = {
            "firstname": "A",
            "lastname": "",
            "email": 123,
            "password": 123
        }

        self.assertFalse(owner_register(obj))
