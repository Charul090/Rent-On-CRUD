import unittest
from ..main.services.owner import delete_property


class DeletePropertyTest(unittest.TestCase):

    def test_delete_success(self):
        obj = {
            "id": 3
        }

        self.assertTrue(delete_property(obj))

    def test_delete_empty(self):
        obj = {}

        self.assertFalse(delete_property(obj))

    def test_delete_type_check(self):
        obj = {
            "id": "3"
        }

        self.assertFalse(delete_property(obj))
