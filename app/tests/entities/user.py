import unittest
from app.entities.user import User


class UserTestCase(unittest.TestCase):

    def test_user_init(self):
        username, email, password = 'a', 'b', 'c'
        obj = User(username, email, password)
        self.assertEqual(obj.username, username)
        self.assertEqual(obj.email, email)
        self.assertEqual(obj.password, password)
        self.assertEqual(obj.is_active, 0)
        self.assertEqual(obj.verified_email, 0)
        self.assertIsNone(obj.last_login)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
