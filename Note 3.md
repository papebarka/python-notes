# Functions, Modules and Packages

Functions may contain multiple lines of instruction.

Modules may contain multiple functions.

### Functions
Declaration

They are declared with the def keyword the assigned a name with parameter lists.

def function_name(params1, params2, ..., paramsN):
	instructions
	instructions
	instructions
	instructions

#### Parameters with default value

def function_name(name, age=18)
	instructions
	instructions

#### Docstrings

They are part of documenting the code.
When we call help(function_name), the docstring declared within the function is returned.

def function_name():
	"""Ceci est un docstring"""


#### Function Signature

Function signature is what helps identifying the so-called function.

In C++ a function signature is comprised of its name and its parameters types, meaning we can have many functions with same name but different parameters.

In python, there is no parameter type. The function signature is only its name. This means we cannot delcare two functions with the same name. If we do, the former is simply erased in favor of the latter.

#### Return

The return instruction means the function returns some values we might stock in a variable.

We are able to return multiple variables we separate by commas.

#### Lambda functions

Lambda is used to declared functions when we want a rather short function declaration in contrast to def which might be longer.

Lambda fnctions are declared with lambda keyword.

Syntax:

lambda param1: instruction

Ex:

lambda x: x*x

f = lambda z,w: z-w
f(10, 4)

### Modules

Modules are python files that contain multiple function declared within them, which can then be used by some other programs.

#### The import method

We can use the "import" method to import modules in our code.

Ex:

import math

math.sqrt(16)


We can use help() method to learn more about modules and functions.

Ex:

help("math")

We can change the module name in the current namespace

Ex:

import math as mathematics

We can also import specific functions or variables from our module

Ex:

from math import sqrt, fabs

We can also import all functions and variables from our module.

Ex:

from math import *


#### Testing module functions within the module itself

Inside a module, if we call to execution a function defined there, whenever we import the module to another code the function is automatically called. To prevent this code execution, we test against __name__ == "__main__"

Ex:

if __name__ == "__main__":
	my_function()

#### Tips

To pause a CLI application before closing, one should use the system function from the os package and pause it.

import os

os.system("pause")

### Packages

Packages are used to group multiple modules just as modules group multiple functions and variables.

Ex:

Package

SubPackage1 > module1

SubPackage1 > module2

SubPackage2 > module1

In Python:

> import package.subpackage2.module1

Initialization file

In folders intended to be used as packages, we often find an initialization file: __init__.py

Haing this file has been optional since python v3.3

