import unittest
from app.entities.role import Role


class RoleTestCase(unittest.TestCase):

    def test_role(self):
        name, description = 'a', 'b'
        obj = Role(name, description)
        self.assertEqual(obj.name, name)
        self.assertEqual(obj.description, description)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)


    def test_none_description(self):
        name, description = 'a', 'b'
        obj = Role(name)
        self.assertEqual(obj.name, name)
        self.assertIsNone(obj.description)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
