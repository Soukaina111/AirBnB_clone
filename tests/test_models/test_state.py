#!/usr/bin/python3
""" this is a unittest for subclass State """


import unittest
from models.state import State

class TestStateModel(unittest.TestCase):
     """ this is a unittest for subclass State """

def test_state(self):
        """ this is a unittest for subclass State """
        state = State()
        state.name = "Morocco"
        self.assertEqual(state.name, "Morocco")

if __name__ == "__main__":
    unittest.main()
