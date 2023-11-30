0x02. Python - import & modules

Why Python programming is awesome:
Readability: Python code is easy to read and write, emphasizing readability and reducing the cost of program maintenance.

Versatility: Python is a versatile language used for web development, data science, artificial intelligence, automation, and more.

Large Standard Library: Python comes with a comprehensive standard library that provides modules and packages for various tasks, reducing the need for external dependencies.

Community Support: Python has a large and active community, which means plenty of resources, libraries, and support are available.

Cross-Platform: Python is compatible with major operating systems, allowing code to run on different platforms without modification.

Productivity: Python's simplicity and high-level abstractions enhance development speed, making it a productive language.

How to import functions from another file:
Assuming you have a Python file named my_module.py:

`
def greet(name):
    print(f"Hello, {name}!")

def square(x):
    return x * x
`

You can import and use functions in another file, e.g., main.py:

`# main.py
from my_module import greet, square

greet("Alice")
result = square(5)
print(result)
`

How to use imported functions:
Once functions are imported, you can use them just like any other functions:

`
# main.py
from my_module import greet, square

greet("Bob")
result = square(3)
print(result)
`

How to create a module:
A module is a Python file containing code you want to reuse. For example, my_module.py is a module in the previous example.

How to use the built-in function dir():
The dir() function is used to get a list of names in the current local scope or the attributes of an object. For example:

`
# Using dir() in the interactive interpreter
dir()
`

How to prevent code in your script from being executed when imported:
You can use the if __name__ == "__main__": construct to ensure that certain code only runs when the script is executed directly, not when it's imported as a module:

`
# my_module.py
def some_function():
    print("This will be executed when imported.")

if __name__ == "__main__":
    print("This will only be executed if the script is run directly.")
`

How to use command line arguments with your Python programs:
Use the sys.argv list or the argparse module to handle command line arguments. Here's a basic example using sys.argv:

`
# script.py
import sys

if len(sys.argv) > 1:
    print("Argument passed:", sys.argv[1])
else:
    print("No arguments passed.")
`

Run it with python script.py argument.


Basic overview of modules in Python:

Creating a Module:

Create a new Python file with a .py extension.
Define functions, classes, or variables in this file.
Example (mymodule.py):

`
# mymodule.py
def greet(name):
    print(f"Hello, {name}!")

def square(x):
    return x * x
`

Using a Module:

To use the functions or variables defined in a module, you need to import the module.
You can import the entire module or specific functions/classes/variables.
Example (main.py):

`
# main.py
import mymodule

mymodule.greet("Alice")
result = mymodule.square(5)
print(result)
`

Importing Specific Items:

You can import specific items from a module using the from ... import ... syntax.
Example:

`
# main.py
from mymodule import greet, square

greet("Bob")
result = square(3)
print(result)
Module Aliases:
`

You can use aliases to make module names shorter.
Example:

`
# main.py
import mymodule as mm

mm.greet("Charlie")
result = mm.square(4)
print(result)
Built-in Modules:
`

Python comes with many built-in modules that provide additional functionality.
Examples include math, random, datetime, etc.
Example:

`
# main.py
import math

print(math.sqrt(25))
`

Executing Modules as Scripts:

You can write a module so that it can be both used as a standalone script and imported as a module.
Example (mymodule.py):

`
# mymodule.py
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    # This block will only execute if the module is run as the main program
    greet("World")
`

When you run mymodule.py as a script, the greet("World") line will execute. If you import mymodule in another script, that block won't execute


Command Line Arguments

Command line arguments are values passed to a script or program when it is run in the command line or terminal. They allow you to provide input to a program when it starts, influencing its behavior or providing data for processing. In Python, you can access command line arguments using the sys.argv list provided by the sys module.

Here's a basic overview:

Using sys.argv:

The sys.argv list in the sys module contains the command-line arguments passed to the script.
The first element (sys.argv[0]) is the script name itself, and the subsequent elements are the arguments.
Example (script.py):

`
# script.py
import sys

# Print the script name
print("Script name:", sys.argv[0])

# Print command line arguments
print("Arguments:", sys.argv[1:])
If you run this script from the command line with python script.py arg1 arg2, you'll get:
`

`
Script name: script.py
Arguments: ['arg1', 'arg2']
`

Parsing Command Line Arguments:

While sys.argv provides access to raw command line arguments, the argparse module is commonly used for more sophisticated argument parsing.
Example (argparse_example.py):

`
# argparse_example.py
import argparse

parser = argparse.ArgumentParser(description="An example script with command line arguments.")
parser.add_argument('name', help='Name to greet')
parser.add_argument('--age', type=int, help='Age of the person')

args = parser.parse_args()

print(f"Hello, {args.name}!")
if args.age:
    print(f"You are {args.age} years old.")
`

If you run this script with python argparse_example.py John --age 25, you'll get:

`
Hello, John!
You are 25 years old.
`

Positional and Optional Arguments:

Positional arguments are mandatory and are usually specified without a flag.
Optional arguments (or flags) are specified with a -- prefix and can have default values.
Help Information:

argparse automatically generates help information based on the arguments you define.
You can view the help by running the script with the -h or --help flag.
Example:

`
python argparse_example.py -h
`

This will display information about the script's usage and available arguments.

Command line arguments are essential for making your scripts more versatile and allowing users to customize their behavior without modifying the script itself. The argparse module provides a powerful and user-friendly way to handle command line arguments in Python.
