import unittest
from ..main.services.message import send_message


class SendMessageTest(unittest.TestCase):

    def test_send_success(self):
        obj = {
            "ancestor": 1,
            "descendnt": 2
        }

        self.assertTrue(send_message(obj))

    def test_send_error(self):
        obj = {
            "ancestor": 1
            }

        self.assertFalse(send_message(obj))

    def test_send_empty(self):
        obj = {
            "ancestor": 1,
            "descendnt": ""
        }

        self.assertFalse(send_message(obj))

    def test_send_wrong(self):
        obj = {
            "ancestor": 1,
            "descendnt": "2"
        }

        self.assertFalse(send_message(obj))
