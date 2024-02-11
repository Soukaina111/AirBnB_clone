#!/usr/bin/python3
import unittest
import os
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create State name=California")
            state_id = output.getvalue().strip()
            self.assertTrue(len(state_id) > 0)

    def test_show(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create City state_id=state_id name=San_Francisco")
            city_id = output.getvalue().strip()
            self.assertTrue(len(city_id) > 0)

            self.console.onecmd(f"show City {city_id}")
            expected_output = f"[City] ({city_id}) {'{' + "'state_id': 'state_id', 'name': 'San_Francisco'" + '}'}"
            self.assertEqual(output.getvalue().strip(), expected_output)

    def test_destroy(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create State name=California")
            state_id = output.getvalue().strip()
            self.assertTrue(len(state_id) > 0)

            self.console.onecmd(f"destroy State {state_id}")
            self.assertFalse(os.path.exists("file.json"))

    def test_all(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create State name=California")
            self.console.onecmd("create City state_id=state_id name=San_Francisco")
            self.console.onecmd("create City state_id=state_id name=Los_Angeles")

            self.console.onecmd("all")
            expected_output = "[State] ({'name': 'California', 'id': 'state_id'})\n" \
                              "[City] ({'state_id': 'state_id', 'name': 'San_Francisco', 'id': 'city_id'})\n" \
                              "[City] ({'state_id': 'state_id', 'name': 'Los_Angeles', 'id': 'city_id'})"
            self.assertEqual(output.getvalue().strip(), expected_output)


if __name__ == "__main__":
    unittest.main()
