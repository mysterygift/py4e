# Lists in python can be composed of many different data types, including other lists.
# They are similar but not identical to arrays. Arrays are part of the NumPy python lib.
# Arrays in NumPy must be all of the same data type.
# NumPy arrays support vector operations like element-by-element addition and multiplication.
# These vector operations are much faster than their core lib counterparts (e.g. numpy.sin or numpy.exp).
# Importantly – adding one or more elements to a NumPy array destroys the previous array and creates a new one, therefore it is less efficient to have
    # multiple large arrays. It is most efficient to create a list and then convert it into an array afterwards when the list is complete.

# Strings are "immutable" – we cannot change their contents. We must make a new string.
# Lists ARE mutable, being able to change their contents using the index operator.
# Each index maps to an element in a list. Any integer expression can be used as an index.

lotto_tickets = [40, 73, 98, 2, 8, 17, 38, 56]
print(lotto_tickets)
lotto_tickets[3] = 69 # Lists are zero-indexed, so this changes the FOURTH item in the list.
print(lotto_tickets) # Prints [40, 73, 98, *69*, 8, 17, 38, 56] – note the change!

# range() returns a list of numbers ranging from zero to a specified number. This is useful for constructing lists to be used in for loops that iterate through items in a list.

print(list(range(4))) # Note that you have to encapsulate range() with a list() from Python3 onwards!
# Outputs [0, 1, 2, 3]

for ticket in lotto_tickets :
    print(f'The winner is ticket number {ticket}. Congratulations!')

for i in range(len(lotto_tickets)) :
    ticket = lotto_tickets[i]
    print(f'You lose, ticket number {ticket}.\nSorry!')

# Two ways of achieving the same thing. The only difference is that the second one goes through the positions in the created range, whilst the first one goes through the items themselves.

# You can also have nested lists (lists WITHIN lists!) These are similar to 2D arrays.

nested_example = [['smoke', 'weed'],['every', 'day', "y'all"]]
print(nested_example[0][1]) # Prints 'weed'.
print(nested_example[1][-2]) # If an index is negative, it counts from the END of a list (but strangely it is NOT zero-indexed when used like this.)

# In statements also work with lists, however if you want to check for an element contained in a subset, you must state this. For example:
'smoke' in nested_example # Returns false
'smoke' in nested_example[0] # Returns true

# The + operator concatenates lists. * repeats a list a given number of times.
listA = [1, 2, 3]
listB = [4, 5, 6]
listC = listA + listB
print(listC) # [1, 2, 3, 4, 5, 6]
print(listC * 2) # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

# The slice : operator works on lists (just like strings). It allows you to provide a range that goes UP TO but DOES NOT INCLUDE provided values.
sliceList = ['any', 'list', 'in', 'python', 'can', 'be', 'SLICED!', 69]
print(sliceList[:4]) # any, list, in, python
print(sliceList[2:6]) # in, python, can, be – Up to but NOT INCLUDING element 6.
print(sliceList[5:]) # be, SLICED!, 69
print(sliceList[:]) # prints the entire list.

# Since lists are mutable, it's useful to make a copy of the list before making changes that fold, spindle or mutilate lists.