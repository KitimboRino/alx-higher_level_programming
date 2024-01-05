0x09. Python - Everything is object

### 1. Why Python programming is awesome:
Python is awesome for several reasons, including its readability, simplicity, versatility, and a vast ecosystem of libraries. It allows for rapid development, and its syntax emphasizes code readability and expressiveness.

```
print("Python is awesome!")
```

### 2. What is an object:
In Python, everything is an object. An object is an instance of a class and can represent data or code.

```
# Example of an object
number = 42
print(type(number))  # <class 'int'>
```

### 3. Difference between a class and an object or instance:
A class is a blueprint for creating objects. An object, also called an instance, is a concrete occurrence of a class.

```
# Class definition
class Dog:
    def bark(self):
        print("Woof!")

# Creating an object (instance) of the class
my_dog = Dog()
my_dog.bark()  # Outputs: Woof!
```

### 4. Difference between immutable and mutable objects:
Mutable objects can be modified after creation, while immutable objects cannot. Lists are mutable, and tuples are immutable.

```
# Mutable object (list)
mutable_list = [1, 2, 3]
mutable_list[0] = 99
print(mutable_list)  # Outputs: [99, 2, 3]

# Immutable object (tuple)
immutable_tuple = (1, 2, 3)
# The following line would raise an error: immutable_tuple[0] = 99
```

### 5. What is a reference:
A reference is a value that refers to an object in memory.

```
x = [1, 2, 3]  # x is a reference to a list object
```

### 6. What is an assignment:
An assignment is the process of binding a name to a value in Python.

```
x = 42  # Assigning the value 42 to the variable x
```

### 7. What is an alias:
An alias is when two or more variables refer to the same object.

```
a = [1, 2, 3]
b = a  # b is now an alias for a
```

### 8. How to know if two variables are identical:
Use the `is` keyword to check if two variables reference the same object.

```
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # Outputs: False
```

### 9. How to know if two variables are linked to the same object:
Use the `==` operator to check if two variables have the same value, and `is` to check if they reference the same object.

```
a = [1, 2, 3]
b = a
print(a == b)  # Outputs: True (same value)
print(a is b)  # Outputs: True (same object)
```

### 10. How to display the variable identifier (memory address):
Use the `id()` function to get the identity (memory address) of an object.

```
x = [1, 2, 3]
print(id(x))  # Outputs something like: 140284805358144
```

### 11. Mutable and immutable:
Mutable objects can be changed after creation (e.g., lists), while immutable objects cannot be modified (e.g., tuples).

### 12. Built-in mutable types:
Examples include lists, dictionaries, and sets.

```
my_list = [1, 2, 3]
my_dict = {'key': 'value'}
my_set = {1, 2, 3}
```

### 13. Built-in immutable types:
Examples include integers, floats, strings, and tuples.

```
my_int = 42
my_float = 3.14
my_str = 'Hello'
my_tuple = (1, 2, 3)
```

### 14. How Python passes variables to functions:
Python passes variables to functions using a mechanism called "pass-by-object-reference." It passes references to objects, and changes made to mutable objects inside a function affect the original object.

```
def modify_list(my_list):
    my_list.append(4)

original_list = [1, 2, 3]
modify_list(original_list)
print(original_list)  # Outputs: [1, 2, 3, 4]
```
