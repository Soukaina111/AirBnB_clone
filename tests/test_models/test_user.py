#!/usr/bin/python3
""" this is a unittest for subclass User """

import unittest
from uuid import uuid4
from models.user import User



class TestUserModel(unittest.TestCase):
    """ this is a unittest for subclass User """

def test_state(self):
    user_id = uuid4()
    user1 = User()
    user1.first_name = "WALID"
    user1.password = "SIRSIRSIR"
    user1.email ="head.avocado@gmail.com"
    user1.last_name = "REGRAGUI"
    self.assertEqual(user1.first_name, "WALID")
    self.assertEqual(user1.last_name, "REGRAGUI")
    self.assertEqual(user1.password, "SIRSIRSIR")
    self.assertEqual(user1.email, "head.avocado@gmail.com")



if __name__ == "__main__":
    unittest.main()

   


