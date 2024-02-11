#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    This class represents a command-line interface for managing objects.

    It provides various commands for creating, retrieving, updating, and deleting objects.
    """

    prompt = "(hbnb) "

    def do_show(self, arg):
        """
        Retrieve and display the details of a specific instance.

        Usage: show <class name> <object id>
        """
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        objects = storage.all()
        key = "{}.{}".format(class_name, obj_id)
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_create(self, arg):
        """
        Create a new instance of a class and save it.

        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        class_name = arg
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        obj = storage.classes[class_name]()
        obj.save()
        print(obj.id)

    def do_destroy(self, arg):
        """
        Delete a specific instance.

        Usage: destroy <class name> <object id>
        """
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        objects = storage.all()
        key = "{}.{}".format(class_name, obj_id)
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """
        Update the attributes of a specific instance.

        Usage: update <class name> <object id> <attribute name> <value>
        """
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        objects = storage.all()
        key = "{}.{}".format(class_name, obj_id)
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        value = args[3]
        obj = objects[key]
        setattr(obj, attribute_name, value)
        obj.save()

    def do_all(self, arg):
        """
        Display all instances or instances of a specific class.

        Usage: all [class name]
        """
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        class_name = arg
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        filtered_objects = [str(obj) for obj in objects.values() if isinstance(obj, storage.classes[class_name])]
        print(filtered_objects)

    def do_quit(self, arg):
        """
        Quit the command-line interface.
        """
        print()
        return True

    def do_EOF(self, arg):
        """
        Handle the end-of-file signal to exit the command-line interface.
        """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
