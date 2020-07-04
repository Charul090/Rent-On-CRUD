import unittest
from ..main.services.owner import add_property


class AddPropertyTest(unittest.TestCase):

    def test_add_success(self):
        obj = {
            "area": 24,
            "amenities": ["swimming pool", "parking"],
            "bedrooms": 4,
            "furnishing": True,
            "address": "Koramangala, Bangalore",
            "price": 20000000
        }

        self.assertTrue(add_property(obj))

    def test_add_error(self):
        obj = {
            "bedrooms": 4,
            "furnishing": True,
            "address": "Koramangala, Bangalore",
            "price": 20000000
        }

        self.assertFalse(add_property(obj))

    def test_add_empty(self):
        obj = {
            "area": "",
            "amenities": ["swimming pool", "parking"],
            "bedrooms": 4,
            "furnishing": True,
            "address": "Koramangala, Bangalore",
            "price": 20000000
        }

        self.assertFalse(add_property(obj))

    def test_add_wrong(self):
        obj = {
            "area": "234",
            "amenities": ["swimming pool", "parking"],
            "bedrooms": 4,
            "furnishing": True,
            "address": "Koramangala, Bangalore",
            "price": 20000000
        }

        self.assertFalse(add_property(obj))
