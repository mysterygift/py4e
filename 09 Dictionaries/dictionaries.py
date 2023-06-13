# A collection is when we have a variable that we can store multiple pieces of information in them.
# A dictionary in Python is another form of collection.
# Lists are linear collection of values that stay in order.
# Dictionaries are a bag of values, each with their own label, and you retrieve values using 'keys'.
# They allow us to do conduct fast database-like ops in Python.
# They have different names in other languages:
    # Associative Arrays - Perl/PHP
    # Properties/Map/HashMap - Java
    # Property Bag - C#/.NET

# 'Associative' refers to the relationship between the key referring to a value.

wallet = dict() # Constructs a dictionary.
wallet['money'] = 12 # Initialises a value of 12 with key 'money'.
wallet['sweets'] = 3
wallet['tissues'] = 75
print(wallet) # {'money': 12, 'sweets': 3, 'tissues': 75}

# We can carry out operations on values stored in dictionaries:

wallet['money'] = wallet['money'] + 12039
print(wallet['money'])

# Dictionary literals (constants) are {}.
# You can initiliase one with values and keys already, or just create one using empty {}.
# Association between keys and values is shown with a :

new_dict = { }
print(new_dict)

# Dictionaries will return a traceback error if you reference a key not in a dictionary.
# You can avoid this by checking if a reference is in a dictionary using an in statement.

# Here is some histogram code:

counts = dict() # Constructor
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen'] # List of names as an input. Could be a file that we parse.
for name in names :
    if name not in counts :
        counts[name] = 1 # If name has not yet been counted, add it into the dict.
    else :
        counts[name] += 1 # Else, add 1 to the value referenced by the key 'name'.

print(counts) # {'csev': 2, 'cwen': 2, 'zqian': 1}

# Checking if something is in a dict() and doing different things is so common that it has been included
# as a method .get(x, defaultvalue). In this way, the above code can be shortened:

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1

print(counts) # {'csev': 2, 'cwen': 2, 'zqian': 1}

# You can get a list of keys, values or items (both) from a dictionary.

x = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(list(x)) # ['chuck', 'fred', 'jan']
print(x.keys()) # dict_keys(['chuck', 'fred', 'jan'])
print(x.values()) # dict_values([1, 42, 100])
print(x.items()) # dict_items([('chuck', 1), ('fred', 42), ('jan', 100)]) - Each element here is a tuple.

# TWO ITERATION VARIABLES!
# We can loop through kv pairs in a dict using two itvars.
# Each iteration, the first var is the key and the second is the corresponding value.

x = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for k,v in x.items() : # This only works if you use items as they spit out a list of tuples.
    print(k, v)

# chuck 1
# fred 42
# jan 100

# A common use of dicts is to count the occurence of words in a file, and can be used in more advanced
# text parsing, as shown below. The python .split() method looks for spaces in strings and treats words
# as tokens separated by spaces.

# Thus treating 'soft' and 'soft!' is two distinct words. 'Who' and 'who' would also be considered
# different. We can use the string methods .lower(), .punctuation() and .translate() to solve this.

# STRINGNAME.translate(STRINGNAME.maketrans(fromstr, tostr, deletestr))

# Replace the chars in fromstr with the character in the same pos as tostr, deleting all chars in
# deletestr. fromstr and tostr can be empty strings and deletestr is an optional parameter.

# In this case, we won't specify tostr, using deletestr to remove all punctuation.

import string # Library needed for string methods.

try :
    fname = input('file name: ')
    fhandle = open(fname)

except :
    print(f'File', fname, 'not found.')
    exit()

counts = { } # dict constructor.
for line in fhandle :
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation)) # Compares string line with punctation found in string.punctuation and removes it from line.
    line = line.lower() # Makes string completely lowercase.
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1 # Uses .get() method to check to see if word is found as a key in dict 'counts'.

print(counts)

# Have a look at the domain_counter.py file included here for some notes on my findings while solving this exercise.