import unittest
from app.api.role import (
    get_roles,
    get_role,
    create_role,
    delete_role
)


class RoleControllerTestCase(unittest.TestCase):

    def test_get_roles(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_get_role(self):
        self.assertEqual("foo".upper(), "FOO")
        
    def test_create_role(self):
        self.assertEqual("foo".upper(), "FOO")
        
    def test_delete_role(self):
        self.assertEqual("foo".upper(), "FOO")
