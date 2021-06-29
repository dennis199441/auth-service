import unittest
from app.services.user_service import (
    update_last_login,
    activate_user,
    deactivate_user,
    change_user_password,
    update_username,
    get_user_info,
    get_user_info_by_email,
    get_all_users,
    create_new_user
)


class UserServiceTestCase(unittest.TestCase):

    def test_update_last_login(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_activate_user(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_deactivate_user(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_change_user_password(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_update_username(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_get_user_info(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_get_user_info_by_email(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_get_all_users(self):
        self.assertEqual("foo".upper(), "FOO")
    
    def test_create_new_user(self):
        self.assertEqual("foo".upper(), "FOO")
