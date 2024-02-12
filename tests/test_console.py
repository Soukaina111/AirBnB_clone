#!/usr/bin/python3
import unittest
from console import HBNBCommand
import sys


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.stdout = sys.stdout
        sys.stdout = self._string_io = StringIO()

    def tearDown(self):
        sys.stdout = self.stdout

    def test_create_missing_class_name(self):
        self.console.onecmd('create')
        output = self._string_io.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_create_invalid_class_name(self):
        self.console.onecmd('create InvalidClass')
        output = self._string_io.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_create_valid_class_name(self):
        self.console.onecmd('create BaseModel')
        result = self._string_io.getvalue().strip()
        self.assertTrue(result)

    def test_show_missing_class_name(self):
        self.console.onecmd('show')
        output = self._string_io.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_show_missing_instance_id(self):
        self.console.onecmd('show BaseModel')
        output = self._string_io.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")


if __name__ == '__main__':
    unittest.main()
