# OOP: User perspective

## Dictionaries

Dictionaries are obects that can contain other objects like lists. Each object in a dictionary is associated with a key.

### Creating and editing dictionaries

### Creation

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

### Deleting from dictionaries

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



