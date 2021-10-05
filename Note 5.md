# OOP: User perspective

### Strings

Strings are examples of objects.

A string inherit from the python str class.

The str class offers some methods:

"xyz".lower()

"xyz".upper()

"xyz".capitalize()

"xyz".strip()

"xyz".center(20)

### Formatting and displaying strings

#### First syntax

We can format strings differently than we used to.

```python
print("Ici c'est {0}, la capitale de la {1}".format(ville, pays))
```

It's not an obligation to call the variables in orders.

```python
print("Ici c'est {0}, la capitale du {1}. {0} est une très belle ville".format(ville, pays))
```

In some cases, we have to call the variables in the right order in format.

```python
print("Ici c'est {}, la capitale de la {}".format(ville, pays))
```

#### Second syntax

Instead of using indexes, we can name variables we are going to display.

```python
identity = """
	{first_name}, {last_name},
	{citizenship}""".format(first_name="Adam", \
last_name="Diarra", citizenship="Mali")
print(identity)
```

#### String concatenation

* We can use the "+" operator to concatenate strings.

Ex:

```python
"Je suis" + " " + "un homme."
```

* Python doesn't allow to concatenate string with another data type. We have to convert the other data type to string in order for it to works. It works this way because even though python is dynamically typed, it is also strongly typed.

Ex:

```python
# this will throw an error
"J'ai" + " " + 21 + " " + "ans"
# This will work fine
"J'ai" + " " + str(21) + " " + "ans"
```

the 'str()' method converts an object to string.

#### Browsing through and selecting strings

##### Accessing by index

###### Accessing characters

```python
my_string = "This is a string"
my_string[0] # First character of the string
my_string[2] # Third character of the string
my_string[-1] # Last character of the string
```

###### Browsing with while

```python
my_string = "This is a string"
i = 0
while i < len(my_string):
	print my_string[i]
	i += 1
```

##### Selecting strings (slicing)

We can select part of a string. This operation will return the part specified without changing the original string.

```python
my_string = "This is a string"
my_string[:2] # From the first to the third character (non-included)
my_string[2:] # From the third character (included) to the last one
my_string[2:len(my_string)] # Everything from the string except the first two characters.
```