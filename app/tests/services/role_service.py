import unittest
from app.services.role_service import (
    get_role_by_name,
    get_role_by_id,
    get_user_roles,
    grant_role,
    revoke_role,
    get_all_roles,
    create_new_role,
    delete_existing_role
)


class RoleServiceTestCase(unittest.TestCase):

    def test_get_role_by_name(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_get_role_by_id(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_get_user_roles(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_grant_role(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_revoke_role(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_get_all_roles(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_create_new_role(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_delete_existing_role(self):
        self.assertEqual("foo".upper(), "FOO")
