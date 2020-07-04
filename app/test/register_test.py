import unittest
from app.main.services.user import register


class RegisterTest(unittest.TestCase):

    def register_succ(self):
        self.assertEqual(register(), {"error": False, "message": "Registered Successfully"})


if __name__ == '__main__':
    unittest.main()