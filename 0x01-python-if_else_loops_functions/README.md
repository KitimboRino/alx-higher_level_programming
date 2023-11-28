0x01. Python - if/else, loops, functions

Why Python programming is awesome:
Python is known for its simplicity, readability, and versatility. It has a large standard library, extensive community support, and is widely used in various domains such as web development, data science, machine learning, and more.

Why indentation is so important in Python:
Indentation is a crucial aspect of Python syntax. It is used to define blocks of code, replacing traditional curly braces or keywords. Proper indentation ensures code readability and is a fundamental part of the language's design.

How to use the if, if ... else statements:

`
if condition:
    # code to execute if condition is True
else:
    # code to execute if condition is False
`

How to use comments:

`
# This is a single-line comment
`
`
"""
This is a
multi-line comment
"""
`

How to assign values to variables:

`
variable_name = value
How to use while and for loops:
`

`
while condition:
    # code to execute while condition is True

for variable in iterable:
    # code to execute for each item in the iterable
`

How Python’s for is different from C’s:
Python's for loop is more versatile than C's. It iterates over items in a sequence (e.g., a list), not just over numerical ranges. It simplifies the looping process.

How to use break and continue statements:

`for i in range(10):
    if i == 5:
        break  # exits the loop
    if i % 2 == 0:
        continue  # skips the rest of the loop for even numbers
    # code here executes for odd numbers
`

How to use else clauses on loops:

`
for item in iterable:
    # code for each item
else:
    # code to execute when the loop is exhausted (not interrupted by a break)
`

What does the pass statement do, and when to use it:
The pass statement is a no-operation statement. It is used as a placeholder when syntactically some code is required, but you don't want to execute any statements.

How to use range:

`
for i in range(start, stop, step):
    # code using i
`
What is a function and how to use functions:

`def my_function(parameter1, parameter2):
    # code
    return result
`
What does return a function that does not use any return statement:
If a function doesn't use a return statement, it implicitly returns None.

Scope of variables:
Variables have local or global scope. A variable defined inside a function has local scope, while one defined outside functions has global scope.

What’s a traceback:
A traceback is a report that shows the sequence of function calls that led to an error. It helps identify the location and cause of an exception.

What are the arithmetic operators and how to use them:
Common arithmetic operators include +, -, *, /, % (modulo), // (floor division), and ** (exponentiation). They are used for basic mathematical operations.
