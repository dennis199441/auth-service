import unittest
from app.entities.user_roles import UserRole


class UserRoleTestCase(unittest.TestCase):

    def test_user_role(self):
        user_id, role_id = 1, 1
        obj = UserRole(user_id, role_id)
        self.assertEqual(obj.user_id, user_id)
        self.assertEqual(obj.role_id, role_id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)


    def test_missing_args(self):
        user_id = 1
        self.assertRaises(TypeError, UserRole, user_id)
        
    def test_missing_all_args(self):
        role_id = 1
        self.assertRaises(TypeError, UserRole)
