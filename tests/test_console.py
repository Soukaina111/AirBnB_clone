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

class TestUpdateCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_update_existing_instance(self):
        # Test updating an existing instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # Create a new instance
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            instance_id = output

            # Update the existing instance
            self.console.onecmd(f'update BaseModel {instance_id} name "New Name"')

            # Check if the instance was updated
            self.console.onecmd(f'show BaseModel {instance_id}')
            output = fake_out.getvalue().strip()
            self.assertIn("name: 'New Name'", output)

    def test_update_nonexistent_instance(self):
        # Test updating a nonexistent instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # Update a nonexistent instance
            self.console.onecmd('update BaseModel 1234 name "New Name"')

            # Check if the error message is displayed
            output = fake_out.getvalue().strip()
            self.assertIn("no instance found", output)

    def test_update_attribute(self):
        # Test updating a specific attribute of an instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # Create a new instance
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            instance_id = output

            # Set an initial attribute value
            self.console.onecmd(f'update BaseModel {instance_id} name "Initial Name"')

            # Update the attribute to a new value
            self.console.onecmd(f'update BaseModel {instance_id} name "Updated Name"')

            # Check if the attribute value was updated
            self.console.onecmd(f'show BaseModel {instance_id}')
            output = fake_out.getvalue().strip()
            self.assertIn("name: 'Updated Name'", output)

    def test_update_multiple_attributes(self):
        # Test updating multiple attributes of an instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # Create a new instance
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            instance_id = output

            # Update multiple attributes
            self.console.onecmd(f'update BaseModel {instance_id} name "New Name" age 25')

            # Check if the attributes were updated
            self.console.onecmd(f'show BaseModel {instance_id}')
            output = fake_out.getvalue().strip()
            self.assertIn("name: 'New Name'", output)
            self.assertIn("age: 25", output)

    def test_update_missing_value(self):
        # Test updating an attribute with a missing value
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # Create a new instance
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            instance_id = output

            # Update an attribute with a missing value
            self.console.onecmd(f'update BaseModel {instance_id} name')

            # Check if the error message is displayed
            output = fake_out.getvalue().strip()
            self.assertIn("value is missing", output)

    def test_update_invalid_attribute(self):
        # Test updating an invalid attribute of an instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # Create a new instance
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            instance_id = output

            # Update an invalid attribute
            self.console.onecmd(f'update BaseModel {instance_id} invalid_attr "New Value"')

            # Check if the error message is displayed
            output = fake_out.getvalue().strip()
            self.assertIn("attribute not found", output)

    def test_update_with_dict(self):
        # Test updating attributes using a dictionary
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # Create a new instance
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            instance_id = output

            # Update attributes using a dictionary
            self.console.onecmd(f'update BaseModel {instance_id} {"{"}name: "New Name", age: 25{"}"}')

            # Check if the attributes were updated
            self.console.onecmd(f'show BaseModel {instance_id}')
            output = fake_out.getvalue().strip()
            self.assertIn("name: 'New Name'", output)
            self.assertIn("age: 25", output)

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_create_command(self):
        # Test the create command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            self.assertEqual(len(output), 36)  # Check if the output is a valid UUID

    def test_show_command(self):
        # Test the show command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            instance_id = output

            self.console.onecmd(f'show BaseModel {instance_id}')
            output = fake_out.getvalue().strip()
            self.assertIn(instance_id, output)

    def test_destroy_command(self):
        # Test the destroy command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            instance_id = output

            self.console.onecmd(f'destroy BaseModel {instance_id}')
            self.console.onecmd(f'show BaseModel {instance_id}')
            output = fake_out.getvalue().strip()
            self.assertIn("no instance found", output)

    def test_all_command(self):
        # Test the all command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create BaseModel')
            self.console.onecmd('create User')
            self.console.onecmd('all')

            output = fake_out.getvalue().strip()
            self.assertIn("BaseModel", output)
            self.assertIn("User", output)

    def test_update_command(self):
        # Test the update command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            instance_id = output

            self.console.onecmd(f'update BaseModel {instance_id} name "New Name"')
            self.console.onecmd(f'show BaseModel {instance_id}')
            output = fake_out.getvalue().strip()
            self.assertIn("name: 'New Name'", output)

    def test_count_command(self):
        # Test the count command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create BaseModel')
            self.console.onecmd('create BaseModel')
            self.console.onecmd('create User')

            self.console.onecmd('count BaseModel')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "2")

            self.console.onecmd('count User')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "1")

    def test_quit_command(self):
        # Test the quit command
        with self.assertRaises(SystemExit):
            self.console.onecmd('quit')

    def test_EOF_command(self):
        # Test the EOF command
        with self.assertRaises(SystemExit):
            self.console.onecmd('EOF')

class TestDestroyCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        storage.delete_all()

    def test_destroy_command_valid_instance(self):
        # Test the destroy command with a valid instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            obj = BaseModel()
            obj.save()
            instance_id = obj.id

            self.console.onecmd(f'destroy BaseModel {instance_id}')

            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

            self.assertIsNone(storage.get('BaseModel', instance_id))

    def test_destroy_command_invalid_instance(self):
        # Test the destroy command with an invalid instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('destroy BaseModel invalid_id')

            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_destroy_command_missing_arguments(self):
        # Test the destroy command with missing arguments
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('destroy')

            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

            self.console.onecmd('destroy BaseModel')

            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')



if __name__ == '__main__':
    unittest.main()
