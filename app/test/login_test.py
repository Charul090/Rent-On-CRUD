import unittest
from ..main.services.user import login as user_login
from ..main.services.owner import login as owner_login


class LoginTest(unittest.TestCase):

    def test_login_success(self):

        obj = {
            "email": "a@gmail.com",
            "password": "hia"
        }

        # self.assertTrue(user_login(obj))
        self.assertTrue(owner_login(obj))

    def test_login_error(self):

        obj = {
            "password": "hia"
        }

        # self.assertFalse(user_login(obj))
        self.assertFalse(owner_login(obj))

    def test_login_type(self):

        obj = {
            "email": 234,
            "password": 123
        }

        # self.assertFalse(user_login(obj))
        self.assertFalse(owner_login(obj))
