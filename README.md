# Air BnB clone - The console

![Air BnB - The Console](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231211%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231211T000559Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9800c59826180f46aebdf7d9c18057931d76edcf51f2d2c53633c25d408ca683)

## Overview

This is the first project in cloning Air BnB, which is an online markert place for short-term and long-term homestays and experiences. It includes a custom command-line interpreter, a file storage engine, and various classes representing different components of the AirBnB system.

## Features

- **BaseModel Class:** The base class for all other classes, includes common attributes and methods.
- **Command-Line Interpreter:** Custom shell (`console.py`) for interacting with the system.
- **File Storage:** Engine for serializing and deserializing instances to and from JSON files.
- **Supported Classes:**
  - `BaseModel`
  - `User`
  - `Place`
  - `State`
  - `City`
  - `Amenity`
  - `Review`


## The Console
This is the command interprater that manages all the objects of this project. It's  functionalities are:
* Creating a new object such as a place or user
* Retrive an object from a file
* Do operations on an object such as count
* Update attributes of an object
* Destroy an object

The console should work in both interactive mode:

``` bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
and non-interactive mode:
``` bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Getting Started

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/airbnb-clone.git
    ```

2. Navigate to the project directory:

    ```bash
    cd airbnb-clone
    ```

## Testing
Unnitests for this project are provided in the `test` folder. To run all the test suites simultaneously run the following command:

``` bash
$ python3 unittest -m discover tests
```
To run specific tests:
``` bash
$ python3 unittest -m tests/test_console.py
```
Alternatively, you can run the tests in non-interactive mode:
``` bash
$ echo "python3 -m unittest discover tests" | bash
```

### Usage

1. Run the command-line interpreter:

    ```bash
    ./console.py
    ```

2. Interact with the shell using supported commands such as `create`, `show`, `destroy`, `all`, `update`, etc.

