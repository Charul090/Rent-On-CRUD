import unittest
from ..main.services.user import login


class LoginTest(unittest.TestCase):

    def test_login_success(self):

        obj = {
            "email": "a@gmail.com",
            "password": "hia"
        }

        self.assertTrue(login(obj))

    def test_login_error(self):

        obj = {
            "password": "hia"
        }

        self.assertFalse(login(obj))

    def test_login_type(self):

        obj = {
            "email": 234,
            "password": 123
        }

        self.assertFalse(login(obj))
