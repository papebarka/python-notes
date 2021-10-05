# OOP: User perspective

## Lists and Tuples

### Lists

Lists are sequences. They may contain many objects/data of same or different data types.

Lists are mutable.

#### Creating lists

There are 2 ways to create lists in python

Ex:

```python
# First way - empty list
my_list = list()
# Second way - empty list
my_list = []
# List with initial data
my_list = [1, "Hello", False, []]
```

Accessing list elements:

Just like with strings, we access list elements by index

```python
my_list = [1, 2, 3, 4]
my_list[0]
```
#### Insertion in list

We can insert data into lists with provided methods. These methods change the original list.

```python
my_list = [1, 2, 3, 4]
my_list.append("Hello") # insert as the last element
my_list.insert(3, 44) # insert 44 at the index 3
```

#### Concatenating lists

We have multiple ways to concatenate lists

```python
my_list = [1, 2, 3, 4]
my_list2 = ['hi', 'we', 'hello']
my_list.extend(my_list2) # insert at the end
my_list + my_list2 # 2nd method with + operator
my_list += my_list2 # similar to extend
```

#### Deleting elements from lists

There are 2 ways to delete element from lists:

* del keyword
* remove method

##### del keyword

del can delete variables as well as elements from list.

```python
my_list = [1, 2, 3, 4]
my_list2 = ['hi', 'we', 'hello']

del my_list2 # deletes my_list2
del my_list[1] # deletes the second element.
```

##### remove method

remove can be used to delete elements from list. The method takes as parameter the element to be deleted.

```python
my_list = [1, 2, 3, 4]
my_list2 = ['hi', 'we', 'hello']

my_list.remove(1)
my_list2.remove('we')
```

#### Looping through lists

We can loop through lists the same way we did with strings

```python
my_list = [1, 2, 3, 4]

# First method
i = 0
while i < len(my_list):
	print(my_list(i))
	i += 1

# Second method
for elt in my_list:
	print(elt)
```

##### The enumerate method

```python
my_list = [1, 2, 3, 4]

for idx, elt in enumerate(my_list):
	print("Index: {}, element: {}".format(idx, elt))

for elt in enumerate(my_list):
	print(elt)
```

The enumerate method returns tuples.

### Tuples

Tuples are immutable lists. They can't change once defined.

#### Definition

```python
# Empty tuple
empty_tuple = ()
# Single element tuple
single = (1,) # For a signle element, we must put the comma at the end
# Non-empty tuple
elements = (1, 2, 6)
```
We often don't work directly on tuples. We can't change them, we can' add into nor delete elements from it.

#### Mechanisms that use tuples

* Multiple assignment

```python
a, b = 3, 4

(a, b) = (3, 4) # Similar to
```

* A function that returns multiple value

```python
def identity():
	age = 10
	name = " Joel Roger"
	return age, name

age, name = identity()
```

<hr>

## Methods for lists and tuples

### Lists methods

#### Conversion between lists and strings

We can convert a string to list and vice versa

```python
# From a string to a list

my_string = "Hello World!"
my_string.split(" ") # returns a lsit

# From a list to a string
my_list = ['Hello', 'World']
" ".join(my_list) # returns a string
```

#### Functions parameters

##### Functions we don't know the number of parameters

If a function takes multiple parameters and we don't know their exact numbers, then we put a * before the name that will take the list of parameters. The parameter will return a tuple of values.

```python
def my_func(*params):
	print(params)

my_func()
```

We can define other parameters next to the list parameter. The other parameters must come before the list parameter.

```python
def my_func(name, age, *params):
	print(age)
	print(name)
	print(params)
```

We can as well define named parameters next to the list parameter. They must come after the list parameter.

```python
def my_func(*params, action='', repeat=3)
```

##### Convert a list into a function parameter

If we have a list or a tuple, we can easily transform/convert them into function parameter (instead of using loop and passing them individually).

Ex:

```python
list_params = [1, 3, 5, 7, 11, 54]
print(*list_params)
```

#### List comprehensions

List comprehensions are ways to filter or modify a list in a simpler way.

##### Easy looping through list

We can loop through a list and returned another with filtered or modified values.

```python
numbers = [0, 1, 2, 3, 4, 5]
[nb * nb for nb in numbers]
```

##### Filtering with a conditional branch

By using conditionalss, we can filter list comprehensions.

```python
numbers = [0, 1, 2, 3, 4, 5]
[nb for nb in numbers if nb%2 == 0]
```



