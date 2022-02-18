# Third section: Object-Oriented Programming

## Ch 17: First approach to classes

Adopting the OOP way is not only a matter of aesthetics but of data modeling. With OOP, we can easily model our program even when it may contain complex structures and data.

### Naming convention

Python's PEP 8 indicates it is preferable to use the **Camel Case** convention to name our classes. Ex: class MyClassName

### Attributes

#### Constructor and attributes

A constructor is a special method defined in our class that is automatically called every time we create an object. It creates our attributes.

In python, special methods are named as such  __MethodName__. There are a many of them.

Ex:

```python
class Person: # Class definition
  """ Class defining a person with the following attributes:
  - name
  - first name
  - age
  - place of residence
  """
  
  def __init__(self): # Constructor
    self.name = "Aladin"
    self.first_name = "Aladin"
    self.age = 29
    self.residence = "Egypt"
    
  
  
  aladin = Person()
  aladin.name
  aladin.firstname
```

In python, the constructor takes as first parameter the self keyword. self relates to the object that's going to be instatiated using our class.
Our constructors can take other parameters as well.

Ex:
```python
class Person: # Class definition
  """ Class defining a person with the following attributes:
  - name
  - first name
  - age
  - place of residence
  """
  
  def __init__(self, name, first_name, age="25", residence="UK"): # Constructor
    self.name = name
    self.first_name = first_name
    self.age = age
    self.residence = residence
    
  
  
  adam = Person("Smith", "Adam")
  adam.residence = "Dakar" # We can change our attribute this way.
```
#### Class attributes

Class attributes are diectly defined in the body of our class. Its value is shared aming all the objects that are instatiated from the class.
To access a class attribute inside or outside the constructor, we prefixe the attribute name by the name of the class.

Ex:

```python
class Person: # Class definition
  """ Class defining a person with the following attributes:
  - name
  - first name
  - age
  - place of residence
  """
  number_of_person = 0
  
  def __init__(self, name, first_name, age="25", residence="UK"): # Constructor
    self.name = name
    self.first_name = first_name
    self.age = age
    self.residence = residence
    Person.number_of_person += 1
    
  
  
  adam = Person("Smith", "Adam")
  Person.number_of_person
  
  john = Person("Erickson", "John")
  Person.number_of_person
```

We can create our own method within classes, just like we'd create them previously.

```python
class Person: # Class definition
  """ Class defining a person with the following attributes:
  - name
  - first name
  - age
  - place of residence
  """
  number_of_person = 0
  
  def __init__(self, name, first_name, age="25", residence="UK"): # Constructor
    self.name = name
    self.first_name = first_name
    self.age = age
    self.residence = residence
    Person.number_of_person += 1
  
  def set_age(self, age):
    self.age = age
  
  
  adam = Person("Smith", "Adam")
  adam.age = 38
```

### The Self Parameter

Self is always the first parameter. Whenever we work on an object method, on the object itself, we'll always use self.

When we call a method on our object, Python will not look for the method in our object but it will directly look in the class defining the object.

Ex:

```python
my_object.my_method(param) => my_method(self, param)
 
```

### Class methods and static methods

We can have class methods the same way we have class attributes. These methods are not working on the **self** instance but on the class itself. Even though rare, class methods can be useful.

We define class methods the same way we do with instance methods except that instead of passing **self** parameter, we pass **cls**.
After that, we use a built-in Python method (classmethod) to specify our method is a class method, not an instance method.

```python
class Car:
  
  created_objects = 0
  
  def __init__(self):
    Car.created_objects += 1
    
  def instance_number(cls):
    print(" We have {} instances.".format(cls.created_objects))
    
  instance_number = classmethod(instance_number)
 
```

We can also define static methods. They resemble class methods except that they take no self nor cls parameter.
They work independently from any data contained within our class or object.

```python
class Test:
  def hello():
    print("This is a static method")
    
   hello = staticmethod(hello)
```

### Introspection

#### dir

Dir is a function that takes an object as a parameter and returns the list of its attributes and methods.

Ex:
```python
dir(my_object)
```
#### Special attribute __dict__

By default, when we write a class, every object derived from that class will have the special attribute __dict__.
This attribute is a dictionary that contains as keys, the name of our attributes and as values, the values of our attribtues.

Ex:
```python
my_object).__dict__
```
