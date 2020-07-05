import unittest
from ..main.services.user import rent


class RentPropertyTest(unittest.TestCase):

    def test_rent_success(self):
        obj = {
            "property_id": 3,
            "time": "2019-07-05 12:52:02",
            "duration": 3
        }

        self.assertTrue(rent(obj))

    def test_rent_empty(self):
        obj = {}

        self.assertFalse(rent(obj))

    def test_rent_type_check(self):
        obj = {
            "property_id": 3,
            "time": "2019-07-05 12:52:02",
            "duration": "3"
        }

        self.assertFalse(rent(obj))
