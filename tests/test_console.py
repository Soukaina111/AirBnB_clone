#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_create_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd('create')
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd('create InvalidClass')
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_create_valid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd('create BaseModel')
            result = output.getvalue().strip()
            self.assertTrue(result)

    def test_show_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd('show')
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_show_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd('show BaseModel')
            self.assertEqual(output.getvalue().strip(), "** instance id missing **")


if __name__ == '__main__':
    unittest.main()
