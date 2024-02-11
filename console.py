#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        print()
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line + ENTER shouldn't execute anything.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of the specified class, saves it,
        and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            cls_name = args[0]
            cls_id = args[1]
            cls = eval(cls_name)
            if cls_name == 'User':
                key = cls_name + "." + cls_id
                if key in storage.all(User).keys():
                    print(storage.all(User)[key])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            cls_name = args[0]
            cls_id = args[1]
            cls = eval(cls_name)
            if cls_name == 'User':
                key = cls_name + "." + cls_id
                if key in storage.all(User).keys():
                    del storage.all(User)[key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representations of instances based on
        the class name, or all instances if no class name is provided.
        """
        if not arg:
            print([str(instance) for instance in storage.all(User).values()])
        else:
            try:
                cls_name = arg
                cls = eval(cls_name)
                if cls_name == 'User':
                    print([str(instance) for key, instance in storage.all(User).items()])
                else:
                    print("** class doesn't exist **")
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating an attribute.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            cls_name = args[0]
            cls_id = args[1]
            cls = eval(cls_name)
            if cls_name == 'User':
                key = cls_name + "." + cls_id
                if key in storage.all(User).keys():
                    if len(args) < 3:
                        print("** attribute name missing **")
                        return
                    attr_name = args[2]
                    if len(args) < 4:
                        print("** value missing **")
                        return
                    attr_value = args[3]
                    instance = storage.all(User)[key]
                    setattr(instance, attr_name, attr_value)
                    instance.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
