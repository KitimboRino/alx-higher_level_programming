**1. Why Python programming is awesome:**

Python is often considered awesome for several reasons. It is a versatile, easy-to-read, and easy-to-learn programming language. Its syntax emphasizes readability, and it supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python has a vast standard library and a large, active community, making it suitable for a wide range of applications, from web development to data analysis and artificial intelligence.

**2. What is a superclass, base class, or parent class:**

A superclass, base class, or parent class in object-oriented programming is a class from which other classes, called subclasses or derived classes, inherit properties and behaviors. The superclass provides a common set of attributes and methods that can be reused by its subclasses.

```
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()  # Inherited from the superclass
```

In this example, `Animal` is the superclass, and `Dog` is the subclass.

**3. What is a subclass:**

A subclass, also known as a derived class, is a class that inherits attributes and methods from another class called the superclass or base class.

```
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()  # Inherited from the superclass
```

In this example, `Dog` is the subclass of the `Animal` superclass.

**4. How to list all attributes and methods of a class or instance:**

You can use the `dir()` function to list all attributes and methods of a class or instance.

```
class MyClass:
    def __init__(self):
        self.my_attribute = 42

    def my_method(self):
        print("Hello, World!")

obj = MyClass()

print(dir(MyClass))  # List attributes and methods of the class
print(dir(obj))      # List attributes and methods of the instance
```

**5. When can an instance have new attributes:**

An instance can have new attributes assigned at any point during its lifetime. You can add new attributes to an instance even after its creation.

```
class MyClass:
    pass

obj = MyClass()
obj.new_attribute = "I'm a new attribute"
print(obj.new_attribute)
```

**6. How to inherit class from another:**

You can inherit a class from another using the parentheses after the class name.

```
class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass
```

`DerivedClass` inherits from `BaseClass`.

**7. How to define a class with multiple base classes:**

You can define a class with multiple base classes by separating them with commas.

```
class Base1:
    pass

class Base2:
    pass

class Derived(Base1, Base2):
    pass
```

`Derived` inherits from both `Base1` and `Base2`.

**8. What is the default class every class inherits from:**

The default class that every class in Python inherits from is the `object` class.

```
class MyClass:
    pass
```

This is equivalent to:

```
class MyClass(object):
    pass
```

**9. How to override a method or attribute inherited from the base class:**

You can override a method or attribute inherited from the base class by redefining it in the subclass.

```
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Overrides the speak method from the base class
```

**10. Which attributes or methods are available by heritage to subclasses:**

Subclasses inherit all attributes and methods from their superclass, except for those that are overridden or explicitly modified in the subclass.

**11. What is the purpose of inheritance:**

The purpose of inheritance is to promote code reuse and create a hierarchy of classes, allowing subclasses to inherit the attributes and methods of a superclass. It facilitates the creation of more specialized classes without duplicating common functionality.

**12. What are, when and how to use isinstance, issubclass, type, and super built-in functions:**

- `isinstance(object, class)` checks if an object is an instance of a class.
  ```
  obj = MyClass()
  print(isinstance(obj, MyClass))
  ```

- `issubclass(class, classinfo)` checks if a class is a subclass of another class.
  ```
  print(issubclass(Derived, Base1))
  ```

- `type(object)` returns the type of an object.
  ```
  obj = MyClass()
  print(type(obj))
  ```

- `super()` returns a temporary object of the superclass, allowing you to call its methods.
  ```
  class Child(Base):
      def some_method(self):
          super().some_method()
  ```

These built-in functions are useful for type checking, inheritance checks, and working with classes and instances in Python.
