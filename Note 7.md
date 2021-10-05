# OOP: User perspective

## Dictionaries

Dictionaries are obects that can contain other objects like lists. Each object in a dictionary is associated with a key.

### Creating and editing dictionaries

#### Creation

```python
# 1st way
my_dictionary = dict()

#2nd way
my_dict = {}
```

Adding key:values to dictionaries

```python
person = {}
person['name'] = "Issa Noah"
```

In a dictionary, we can use almost every data type as key and absolutely every data type as value.

Ex:

We can use tuples as dictionary key. We don't necessarily have to mention the parathensis since they're implied if we omit them.

Ex:

```python
person[1, 'age'] = 56
person[(2, 'age')] = 43
```

We can also create dictionaries with default values:

Ex:

```python
person = {'age': 23, 'name': 'Isaac Keita'}
```

#### Deleting from dictionaries

Similar to lists, there are two ways to delete from dictionaries.

* del keyword
* pop method (for dictionaries)

Ex:

```python
person = {'age': 23, 'name': 'Isaac Keita', 'country': 'Mali'}

# With delete
del person['age']

# With pop
person.pop('country')
```

In additon to deleting the key and associated value, pop also returns the deleted value.


NB: Dictionaries are sometimes used to store functions.

Ex:

```python
def sayHi():
	print("Hi")

def buzz():
	print("Buzz")

# Storing
my_functions = {}
my_functions["hi"] = sayHi
my_functions["bzz"] = buzz

# Calling
my_functions["hi"]()
my_functions["bzz"]()

```
#### Looping through dictionary

* We can loop through a dictionary and get all the keys.

Ex:

```python
animals = {'lions': 15, 'Zebra': 32}

for id_key in animals.keys():
	print(id_key)
```

* We can also loop through a dictionary and get all the values.

Ex:

```python
animals = {'lions': 15, 'Zebra': 32}

for value in animals.values():
	print(value)
```

* We can as well loop through a dictionary and get all the keys and values.

Ex:

```python
animals = {'lions': 15, 'Zebra': 32}

for idx_key, value in animals.items():
	print("key: {} Value: {}".format(idx_key, value))
```
### Dictionaries and function parameters

Similarly to tuples and simple parameters, we can also capture named parameters with dictionaries.

Ex:

```python
def my_parameters(**params):
	print("my named params {}".format(params))
```

We use * for unnamed parameters and ** for named parameters.

Knowing this, we can capture both named and unnamed parameters.

Ex:

```python
def my_parameters(*params, **nparams):
	print("My simple params {} and my named params {}".format(params, nparams))
```

#### We can convert dictionaries into named parameters of a function

Ex:

```python
params = {"sep":" >> ", "end":" -\n " }

print("This", "Is", "Us", "!", **params)
```

To indicate to python the dictionary should be transmitted as a parameter, we put the double star before the name ** in our function call.