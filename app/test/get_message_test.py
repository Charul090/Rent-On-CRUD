import unittest
from ..main.services.message import get_message


class GetMessageTest(unittest.TestCase):

    def test_get_success(self):
        obj = {
            "sender":1,
            "receiver":2
        }

        self.assertTrue(get_message(obj))

    def test_get_error(self):
        obj = {
                "sender":1
            }

        self.assertFalse(get_message(obj))

    def test_get_empty(self):
        obj = {
            "sender":1,
            "receiver":""
        }

        self.assertFalse(get_message(obj))

    def test_get_wrong(self):
        obj = {
            "sender":1,
            "receiver":"2"
        }

        self.assertFalse(get_message(obj))
