# OOP: User perspective

## Files

Reading from and writing to files can be an easy way to save our data and know the current states of the user. I can also be a simple way to save user informations.

### Changing working directory

Working directly in the python interpreter, it's better to change the working directory since the current directory of the CLI interpreter is where the python interpreter executable is located.

To change directory, we call the function 'chdir' from the 'os' module.

```python
import os
os.chdir("C:/my projects")
```

#### Relative and absolute path

* Absolute path: contains the full path (the suit of repertory) to where our file is. It starts at root directory and works down.

* Relative path: It's the path related to the present working directory (pwd). It starts at the current directory.

### Reading from and writing to a file

#### Opening file

To open a file, we use the method 'open' directly available for use in python without importing any module.

The 'open' methods takes as parameters:

- The path to the file (absolute or relative)
- The mode for opening the file.

**Opening Modes**:

- 'r': Read mode
- 'w': Write mode. the content of the file is erased. If the file doesn't exist, it's created.
- 'a': Append write mode. Content is written at the end of the file without erasing the previous content. If the file doesn't exist, its created.

Ex:

```python
notes = open('python_notes', 'r')
```

#### Closing file

To close a file we simply invoke the method 'close()'.

Ex:

```python
notes = open('python_notes', 'a')
notes.close()
```

#### Read the whole file

To read the whole file, we invoke the method 'read()'.

Ex:

```python
notes = open('python_notes', 'a')
notes_content = notes.read()
print(notes_content)
notes.close()
```

#### Writing in a file

To write in a file, we either open it with 'a' or 'w' mode.

##### Writing a string

To write a string, we use the method 'write()' by passing the string as the parameter. It returns the number of characters that has been written.

Ex:

```python
my_file = open('notes', 'w')
my_file.write("Hello, how are you?")
notes.close()
```

##### Writing other data types

The 'write()' methodaccepts only strings.

To write other data types like numbers and others, we'll have to convert them to string before writing them. We'll also have to convert them back to the original data type after reading them.

###### 'with' keyword

Opening files is error prone. We can have many errors while writing in or reading from files.

We might also forget to close the fime after opening it. If we try to reopen the file, we'll not be able to access the file since it was previously open and not closed after use.

To prevent all those erros, we use the keyword 'with'.
'with' is also used when manipulating other objects.

'with' comes before the block in which we're manipulating our file.

Ex:

```python
with open('text', 'r') as my_file:
	contents = my_file.read()
```

If an exception occurs, python will close the file.

With the 'with' keyword, we can check if our file is closed by invoking the 'closed' attribute which will return True if it is.

Ex:

```python
with open('text', 'r') as my_file:
	contents = my_file.read()
	print(my_file.closed)
```

##### Saving objects in files

In Python, we can write in and read from our files any object we want to thanks to the 'pickle' module which gives us the classes Pickler and Unpickler.

```python
import pickle
```

###### Saving an object in a file

To save our object in a file, we use the **Pickler** class to create the object and and the **dump()** method to finally save it.

Ex:

```python
import pickle
game_data = {
	"score1": 32,
	"score2": 45,
	"score3": 67,
}
with open('game', 'wb') as game:
	game_pickler = pickle.Pickler(game)
	game_pickler.dump(game_data)
```

We can give an extension to our file if we wish to.

* *wb: write in binary mode* 

###### Reading our saved object in a file

To read our object from the file, we use the **Unpickler** class. To read the objects, we call the `load()` method of our depickler. the method will return the first read object and if there are many objects, we'll have to invoke it multiple times.

Ex:

```python
import pickle

with open('game', 'rb') as game:
	game_unpickler = pickle.Pickler(game)
	game_data = game_unpickler.load()
```


