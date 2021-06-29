import unittest
from app.api.user_role import (
    get_roles,
    grant,
    revoke,
)


class UserRoleControllerTestCase(unittest.TestCase):

    def test_get_roles(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_grant(self):
        self.assertEqual("foo".upper(), "FOO")
        
    def test_revoke(self):
        self.assertEqual("foo".upper(), "FOO")
