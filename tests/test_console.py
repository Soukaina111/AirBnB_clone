#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage

class TestPrompting(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_prompt_default(self):
        # Teste l'invitation à saisir par défaut
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.cmdloop()
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "(hbnb) ")

    def test_prompt_custom(self):
        # Teste une invitation à saisir personnalisée
        custom_prompt = "(custom_prompt) "
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', return_value='quit'):
                self.console.cmdloop(prompt=custom_prompt)
            output = fake_out.getvalue().strip()
            self.assertEqual(output, custom_prompt)


class TestHelpMessages(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_help_quit(self):
        # Teste le message d'aide pour la commande "quit"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('help quit')
            output = fake_out.getvalue().strip()
            self.assertIn("Quit command to exit the program", output)

    def test_help_create(self):
        # Teste le message d'aide pour la commande "create"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('help create')
            output = fake_out.getvalue().strip()
            self.assertIn("Create a new instance of a BaseModel subclass", output)

    def test_help_show(self):
        # Teste le message d'aide pour la commande "show"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('help show')
            output = fake_out.getvalue().strip()
            self.assertIn("Show information about a specific instance", output)

    def test_help_all(self):
        # Teste le message d'aide pour la commande "all"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('help all')
            output = fake_out.getvalue().strip()
            self.assertIn("Show information about all instances", output)

    def test_help_update(self):
        # Teste le message d'aide pour la commande "update"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('help update')
            output = fake_out.getvalue().strip()
            self.assertIn("Update attributes of a specific instance", output)

    def test_help_destroy(self):
        # Teste le message d'aide pour la commande "destroy"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('help destroy')
            output = fake_out.getvalue().strip()
            self.assertIn("Delete a specific instance", output)

    def test_help_count(self):
        # Teste le message d'aide pour la commande "count"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('help count')
            output = fake_out.getvalue().strip()
            self.assertIn("Get the count of instances of a certain class", output)

    def test_help_help(self):
        # Teste le message d'aide pour la commande "help"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('help help')
            output = fake_out.getvalue().strip()
            self.assertIn("Show help information for a specific command", output)


if __name__ == '__main__':
    unittest.main()
