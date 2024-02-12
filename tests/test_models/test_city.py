#!/usr/bin/python3
""" this is a unittest for subclass City """

import unittest
from uuid import uuid4
from models.city import City

class TestCityModel(unittest.TestCase):
    """ this is a unittest for subclass City """

def test_city(self):
        """ this is a unittest for subclass City """
        state_id = uuid4()
        city = City()
        city.name = "Casablanca"
        city.state_id = state_id
        self.assertEqual(city.name, "Casablanca")
        self.assertEqual(city.state_id, state_id)

if __name__ == "__main__":
    unittest.main()
