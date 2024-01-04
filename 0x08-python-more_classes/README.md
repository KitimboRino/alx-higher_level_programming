0x08. Python - More Classes and Objects Notes

### Why Python programming is awesome
Python is considered awesome for several reasons. It has a clear and readable syntax, extensive libraries and frameworks, a large and supportive community, cross-platform compatibility, and is suitable for various applications, including web development, data science, machine learning, and more.

### What is OOP
OOP stands for Object-Oriented Programming. It is a programming paradigm that uses objects, which are instances of classes, to organize code. OOP promotes concepts such as encapsulation, inheritance, and polymorphism to structure and design code in a modular and reusable way.

### “first-class everything”
In Python, everything is considered a first-class object. This means that functions, classes, and even modules can be treated as objects. They can be assigned to variables, passed as arguments to functions, and returned as values.

### What is a class
A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have. Objects are instances of a class.

### What is an object and an instance
An object is a concrete instantiation of a class. An instance is a specific occurrence of an object.

### What is the difference between a class and an object or instance
A class is a template or blueprint, while an object is a concrete realization of that template. An instance is a specific occurrence of an object.

### What is an attribute
An attribute is a piece of information or data associated with a class or an object.

### What are and how to use public, protected, and private attributes
- Public attributes are accessible from anywhere. They are defined without any prefix.
- Protected attributes have a single leading underscore and are intended for internal use.
- Private attributes have a double leading underscore and are not accessible directly from outside the class.

```python
class MyClass:
    def __init__(self):
        self.public_attr = "I'm public"
        self._protected_attr = "I'm protected"
        self.__private_attr = "I'm private"
```

### What is self
`self` is a convention in Python that represents the instance of the class. It is the first parameter in the method definition and is used to access instance variables within the class.

### What is a method
A method is a function defined within a class. It operates on data associated with the class and is called on instances of the class.

### What is the special __init__ method and how to use it
`__init__` is a special method in Python classes that is automatically called when an object is created. It is used for initializing the attributes of the object.

```python
class MyClass:
    def __init__(self, attribute):
        self.attribute = attribute

obj = MyClass("Initialized")
```

### What is Data Abstraction, Data Encapsulation, and Information Hiding
- **Data Abstraction:** It refers to the concept of hiding the complex implementation details and showing only the necessary features of an object.
- **Data Encapsulation:** It involves bundling the data (attributes) and the methods that operate on the data into a single unit, i.e., a class.
- **Information Hiding:** It is a principle of restricting access to certain details of an object, emphasizing only what is necessary for the external world.

### What is a property
A property is a special kind of attribute that can be accessed using the dot notation, like a regular attribute, but behind the scenes, it may involve getter and setter methods.

### What is the difference between an attribute and a property in Python
An attribute is a piece of data associated with an object, while a property is a special kind of attribute that has getter, setter, and deleter methods associated with it.

### What is the Pythonic way to write getters and setters in Python
The Pythonic way is to use the `@property` decorator for getters, and the `@<property_name>.setter` decorator for setters.

```python
class MyClass:
    def __init__(self):
        self._my_attribute = None

    @property
    def my_attribute(self):
        return self._my_attribute

    @my_attribute.setter
    def my_attribute(self, value):
        self._my_attribute = value
```

### What are the special __str__ and __repr__ methods and how to use them
- `__str__` returns a string representation of an object for the user.
- `__repr__` returns an "official" string representation of an object for developers.

### What is the difference between __str__ and __repr__
`__str__` is called by `str()` and `print()`, while `__repr__` is used by `repr()` and is more for developers and debugging.

### What is a class attribute
A class attribute is an attribute that belongs to the class rather than the instance. It is shared among all instances of the class.

### What is the difference between an object attribute and a class attribute
An object attribute is specific to an instance, while a class attribute is shared among all instances of a class.

### What is a class method
A class method is a method that is bound to the class and not the instance of the class. It is defined using the `@classmethod` decorator.

### What is a static method
A static method is a method that is bound to a class rather than an instance. It is defined using the `@staticmethod` decorator.

### How to dynamically create arbitrary new attributes for existing instances of a class
You can dynamically create new attributes for instances by simply assigning values to new attribute names.

```python
class MyClass:
    pass

obj = MyClass()
obj.new_attribute = "I'm a new attribute"
```

### How to bind attributes to objects and classes
Attributes are bound to objects by assigning values using the dot notation. Class attributes are bound to the class.

```
class MyClass:
    class_attribute = "I'm a class attribute"

obj = MyClass()
obj.object_attribute = "I'm an object attribute"
```

### What is and what does contain __dict__ of a class and of an instance of a class
`__dict__` is a dictionary that contains the namespace of a class or an instance. It holds the attributes and methods of the class or instance.

```
class MyClass:
    class_attribute = "I'm a class attribute"

obj = MyClass()
print(obj.__dict__)  # {'object_attribute': "I'm an object attribute"}
print(MyClass.__dict__)  # {'class_attribute': "I'm a class attribute", ...}
```

### How does Python find the attributes of an object or class
Python looks for attributes first in the instance's namespace, then in the class's namespace, and finally in the namespaces of the class's ancestors (if inheritance is involved).

### How to use the getattr function
`getattr(object, name[, default])` is a built-in function that gets the value of an attribute of an object. It returns the value of the attribute if it exists, or a default value if provided.

```
class MyClass:
    attribute = "I'm an attribute"

obj = MyClass()
value = getattr(obj, 'attribute', 'Default')
print(value)  # "I'm an attribute"
```
