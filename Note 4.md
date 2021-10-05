# Exceptions

Minimum version

```python
try:
	instruction
except:
	instruction
```

More complete version

```python
try:
	instruction
except ErrorType:
	instruction
```

ErrorType can be: NameError, TypeError, ZeroDivisionError, and many others...

We can handle as much exceptions as needed.

```python
try:
	instruction
except ZeroDivisionError:
	instruction
except NameError:
	instruction
```

### else and finally keyword

else

In a `try` block, else executes and instruction if there are no exception handled.

```python
try:
	instruction
except ErrorType:
	instruction
else:
	Anoher Instruction
```

finally

The `finally` block is executed after the try/except block whether there are exception handled or not.

```python
try:
	instruction
except ErrorType:
	instruction
finally:
	Anoher Instruction
```

### pass keyword

We can write pass in a block if don't have instructions to be executed.

Ex:

```python
def my_function():
	pass
```

```python
try:
	instruction
except ErrorType:
	pass
finally:
	pass
```


### Assertions (assert)

Assertions are a way to check whether a condition is true and if not, immediately raises an error (Exception AssertionError).

Python's assert statement is a debugging aid, not a mechanism for handling runtime errors.


```python
age = input("Quel est votre âge?")
try:
	age = int(age)
	assert age > 15
except ValueError:
	print("Vous n'avez pas saisi un nombre")
except AssertionError:
	print("Vous n'avez pas plus de 15 ans")
```

### Raise an exception

With Python, we can raise an exception manually.

Syntax

```python
raise ExceptionType("Custom Message")
```

Ex:

```python
age = input("Quel est votre âge?")
try:
	age = int(age)
	if age <= 0:
		raise ValueError("L'âge ne peut être négative 		ou nulle"
except ValueError:
	print("Vous n'avez pas saisi un nombre")
```

## Module: Random number

To generate random numbers, we use the python function randrange from the module random.

```python
from random import randrange
randrange(6) # Generate random numbe between 0 & 5
randrange(1, 7) # Generate random numbe between 1 & 6
```