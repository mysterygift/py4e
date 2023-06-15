# Function definitions can be used throughout a program (keep in mind the concept of scope).

def func_name() : # You can declare arguments to be passed in within the paranthesis. This full line is called the header.
    print('This is an example of a function in Python.') # This is the function's body.

# Importantly, the first char of a function cannot be a number.
# This function does not return any values - they are void functions.

# When defining and declaring functions that have arguments, these arguments are evaluated
# before the function is executed.

import math

def print_twice(printvar) :
    print(printvar)
    print(printvar)

print_twice(math.cos(math.pi))
# -1.0
# -1.0

# As you can see, cos(pi) = -1.0 is evaluated before it is passed into the f(print_twice).

# Functions that return one or more vars are often much more interesting.

def addtwo(a, b) :
    added = a+b
    secret = b-a
    return added,secret # Returns a tuple! The function returns a function object (which is a value/values returned by a function).

x = addtwo(3,1230) # This function returns the value in variable added and stores it in var(x).
secret = addtwo(3,2)
print(x,secret)

# I altered the function above to return multiple values as a tuple. Convenient!