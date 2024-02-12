#!/usr/bin/python3
""" Starts the entry point of the Airbnb Project-Console
"""
from models import storage
from cmd import Cmd
from models.base_model import BaseModel
from models.user import User
#from models.state import State
#from models.city import City
"""from models.amenity import Amenity
from models.place import Place
from models.review import Review"""

Entities = storage.models


class HBNBCommand(Cmd):
    """ have multiple commands that we overrided """
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """End of file function ovverided"""
        print()
        return True

    def do_quit(self, args):
        """a function that quits the program"""
        print()
        return True

    def emptyline(self):
        """executed when we press enter and do nothing """
        pass

    def do_create(self, line):
        """Creates a new instance of a given model name"""
        line = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in Entities:
            print("** class doesn't exist **")
        elif len(line) == 1:
            searched = eval(line[0])()
            print(searched.id)
            searched.save()
        else:
            print("** Can't create because their is too many arguments **")

    def do_show(self, line):
        """Prints the string representation
        of an instance based on the class name and id"""
        input = line.split()
        if not input:
            print("** class name missing **")
        elif len(input) == 1:
            print("** instance id missing **")
        elif len(input) == 2:
            try:
                obj = storage.search_id(*input)
                print(obj)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many arguments for show **")

    def do_destroy(self, line):
        """Removes an instance of a given entity using id and class model"""
        output = line.split()

        if not output:
            print("** class name missing **")
        elif len(output) == 1:
            print("** instance id missing **")
        elif len(output) == 2:
            try:
                storage.destroy_id(*output)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** There is too  many arguments To destroy **")

    def do_all(self, line):
        """Display string representations
        of all instances of a given class."""
        line = line.split()
        if len(line) < 2:
            try:
                print(storage.retrieve_data(*line))
            except ModelNotFoundError:
                print("** class doesn't exist **")
        else:
            print("** Too many arguments for all **")

    def do_update(self, line):
        """Updates an instance based on its id"""
        input = line.split()
        if len(input) == 0:
            print("** class name missing **")
        elif len(input) == 1:
            print("** instance id missing **")
        elif len(input) == 2:
            print("** attribute name missing **")
        elif len(input) == 3:
            print("** value missing **")
        else:
            try:
                storage.single_modif(*input[0:4])
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
