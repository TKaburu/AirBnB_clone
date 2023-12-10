#!/usr/bin/python3
"""Airbnb console"""
import cmd
from datetime import datetime
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
    """console class"""
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
        """quites console"""
        return True

    def do_EOF(self, args):
        """quits console with CtrlD"""
        print()
        return True

    def emptyline(self):
        """does nothing with empty line + ENTER"""
        pass

    def do_create(self, args):
        """creates a new instance of base model and saves in JSON"""
        if len(args) == 0:
            print("** class name missing **")
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            # create an instance
            instance = eval(args)()
            # save the instance, save method from BaseModel
            instance.save()
            # print the id generated using uuid4
            print(instance.id)

    def do_show(self, args):
        """prints string rep of an instance based on id"""

        arg = args.split()

        if len(arg) < 1:
            print("** class name missing **")
            return

        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        try:
            if arg[1]:
                name = "{}.{}".format(arg[0], arg[1])
                # accesses ID and Name from all function in storage
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, args):
        """
        deletes an instance based on the class name
        and id then saves to the JSON file
        """
        # arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        arg = args.split()
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if len(arg) < 2:
                print("** instance id missing **")
                return
            name = "{}.{}".format(arg[0], arg[1])
            if name not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[name]
                storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, args):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        arg = args.split()
        obj_list = []
        if len(args) == 0:
            # iterates over the object dict in all
            for objs in storage.all().values():
                obj_list.append(str(objs))
            print(obj_list)
        elif arg[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if arg[0] in key:
                    obj_list.append(str(objs))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Update if given exact object, exact attribute"""
        arg = args.split()
        if len(arg) >= 4:
            # sets the key to serch in storage
            key = "{}.{}".format(arg[0], arg[1])
            # type casts to the correct type
            cast = type(eval(arg[3]))
            arg3 = arg[3].strip('"').strip("'")
            # sets atts in the dict
            setattr(storage.all()[key], arg[2], cast(arg3))
            # saves the updates in storage
            storage.all()[key].save()
        elif len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(arg[0], arg[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, args):
        """Display count of instances specified"""
        if args in HBNBCommand.classes:
            count = 0
            for key, objs in storage.all().items():
                if args in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """Accepts class name followed by arguement"""
        args = line.split('.')
        class_arg = args[0]
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(line))
            return
        try:
            args = args[1].split('(')
            command = args[0]
            if command == 'all':
                HBNBCommand.do_all(self, class_arg)
            elif command == 'count':
                HBNBCommand.do_count(self, class_arg)
            elif command == 'show':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_show(self, arg)
            elif command == 'destroy':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip('"')
                id_arg = id_arg.strip("'")
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_destroy(self, arg)
            elif command == 'update':
                args = args[1].split(',')
                id_arg = args[0].strip("'")
                id_arg = id_arg.strip('"')
                name_arg = args[1].strip(',')
                val_arg = args[2]
                name_arg = name_arg.strip(' ')
                name_arg = name_arg.strip("'")
                name_arg = name_arg.strip('"')
                val_arg = val_arg.strip(' ')
                val_arg = val_arg.strip(')')
                arg = class_arg + ' ' + id_arg + ' ' + name_arg + ' ' + val_arg
                HBNBCommand.do_update(self, arg)
            else:
                print("*** Unknown syntax: {}".format(line))
        except IndexError:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
