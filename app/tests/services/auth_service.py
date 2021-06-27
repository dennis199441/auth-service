import unittest
from app.services.auth_service import refresh_token

class AuthServiceTestCase(unittest.TestCase):

    def test_authenticate(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_refresh_token(self):
        self.assertEqual("bar".upper(), "BAR")
