#!/usr/bin/python3
""" this is a unittest for subclass Amenity """

import unittest
from models.amenity import Amenity


class TestAmenityModel(unittest.TestCase):
    """ this is a unittest for subclass Amenity """

def test_amenity(self):
        amenity = Amenity()
        amenity.name = "Payed Subscription"
        self.assertEqual(amenity.name, "Payed Subscription")

if __name__ == "__main__":
    unittest.main()
