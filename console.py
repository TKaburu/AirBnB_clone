#!/usr/bin/python3

""" Import necessary models """


import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ This class defines the command interprater. it uses cmd built-in """
    prompt = "(hbnb) "

    classes = {"BaseModel": BaseModel,
                 "User": User,
                 "Place": Place,
                 "State": State,
                 "City": City,
                 "Amenity": Amenity,
                 "Review": Review

                }

    def do_quit(self, args):
        """ This method quits the custom shell """
        return True

    do_EOF = do_quit

    def do_create(self, args):
        """
        This method create a new instance of BaseModel,
        save it, and print the id
        """

        # class name is missing
        if args is None or len(args) == 0:
            print("** class name missing **")

        # if the class name is not part of the above classes then it doesn't exist
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
        
        else:
            # 1st create new object of the specific class
            # save the new object
            # print new objects id

            obj = self.classes[args]()
            models.storage.save()
            print(obj.id)
    
    def do_show(self, args):
        """
        """

        # split the arguments passed. We want to have separeted words
        arg = args.split()

        # Check if class name is missing
        if len(arg) == 0:
            print("** class name missing **")
        else:
            nameof_class = arg[0] # This is the class name since its the 1st index

            # if the class name is not part of the above classes then it doesn't exist
            if nameof_class not in HBNBCommand.classes:
                print("** class doesn't exist **")

            elif len(arg) == 1:
                # instance id is missing
                print("** instance id missing **")
            else:
                instance_id = arg[1]

                # Get the instance using the class name and id
                key = f"{nameof_class}.{instance_id}"
                instances = models.storage.all()
                instance = instances.get(key)

                if instance:
                    print(instance)
                else:
                    print("** no instance found **")

    def do_all(self, args):
        """Prints the string representations of instances."""

        arg = arg.split()
        nameof_class = arg[0]

        if len(nameof_class) == 0 or nameof_class not in HBNBCommand.classes:
            print("** class doesn't exist **")

        # not complete


if __name__ == '__main__':
    HBNBCommand().cmdloop()
