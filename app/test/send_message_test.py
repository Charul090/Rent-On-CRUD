import unittest
from ..main.services.message import send_message


class SendMessageTest(unittest.TestCase):

    def test_send_success(self):
        obj = {
            "sender_id": 1,
            "receiver_id": 2,
            "message": "Hi there I am Aman!"
        }

        self.assertTrue(send_message(obj))

    def test_send_error(self):
        obj = {
            "sender_id": 1,
            "receiver_id": 2
        }

        self.assertFalse(send_message(obj))

    def test_send_empty(self):
        obj = {
            "sender_id": 1,
            "receiver_id": "",
            "message": "Hi there I am Aman!"
        }

        self.assertFalse(send_message(obj))

    def test_send_wrong(self):
        obj = {
            "sender_id": 1,
            "receiver_id": "2",
            "message": "Hi there I am Aman!"
        }

        self.assertFalse(send_message(obj))
