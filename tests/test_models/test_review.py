#!/usr/bin/python3
""" this is a unittest for subclass Review """

import unittest
from uuid import uuid4
from models.review import Review




class TestReviewModel(unittest.TestCase):
    """ this is a unittest for subclass Review """


def test_review(self):
        """ this is a unittest for subclass Review """
        place_id = uuid4()
        user_id = uuid4()
        review = Review()
        review.place_id = place_id
        review.user_id = user_id
        review.text = "Not bad needs some adjustements"
        self.assertEqual(review.place_id, place_id)
        self.assertEqual(review.user_id, user_id)
        self.assertEqual(review.text, "Not bad needs some adjustements")

if __name__ == "__main__":
    unittest.main()
