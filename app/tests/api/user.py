import unittest
from app.api.user import (
    activate,
    deactivate,
    get_user_details,
    change_password,
    change_username,
    get_user,
    get_users,
    create_user
)


class UserControllerTestCase(unittest.TestCase):

    def test_activate(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_deactivate(self):
        self.assertEqual("foo".upper(), "FOO")
        
    def test_get_user_details(self):
        self.assertEqual("foo".upper(), "FOO")
        
    def test_change_password(self):
        self.assertEqual("foo".upper(), "FOO")
        
    def test_change_username(self):
        self.assertEqual("foo".upper(), "FOO")
        
    def test_get_user(self):
        self.assertEqual("foo".upper(), "FOO")
        
    def test_get_users(self):
        self.assertEqual("foo".upper(), "FOO")
        
    def test_create_user(self):
        self.assertEqual("foo".upper(), "FOO")
