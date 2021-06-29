import unittest
from app.api.auth import (
    login,
    refresh
)


class AuthControllerTestCase(unittest.TestCase):

    def test_login(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_refresh(self):
        self.assertEqual("foo".upper(), "FOO")
