#!/usr/bin/python3
""" Starts the entry point of the Airbnb Project-Console
"""

from cmd import Cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
