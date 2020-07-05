import unittest
from ..main.services.owner import update_property


class UpdatePropertyTest(unittest.TestCase):

    def test_update_success(self):
        obj = {
            "area": 24,
            "amenities": ["swimming pool", "parking"],
            "bedrooms": 4,
            "furnishing": True,
            "address": "Koramangala, Bangalore",
            "price": 20000000,
            "id": 1
        }

        self.assertTrue(update_property(obj))

    def test_update_error(self):
        obj = {
            "bedrooms": 4,
            "furnishing": True,
            "address": "Koramangala, Bangalore",
            "price": 20000000
        }

        self.assertFalse(update_property(obj))

    def test_update_empty(self):
        obj = {
            "area": "",
            "amenities": ["swimming pool", "parking"],
            "bedrooms": 4,
            "furnishing": True,
            "address": "Koramangala, Bangalore",
            "price": 20000000,
            "id": 1
        }

        self.assertFalse(update_property(obj))

    def test_update_wrong(self):
        obj = {
            "area": "234",
            "amenities": ["swimming pool", "parking"],
            "bedrooms": 4,
            "furnishing": True,
            "address": "Koramangala, Bangalore",
            "price": 20000000,
            "id": 1
        }

        self.assertFalse(update_property(obj))
