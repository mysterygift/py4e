# .split() breaks a string into parts and produces a list of strings.
# We can think of the elements in this list as words.
# We can access a particular word or loop through each word.

abc = 'These three words.'
stuff = abc.split() # Strings aren't mutable, so we write the list into a new variable.
print(len(stuff)) # 3
print(stuff[2]) # words.

# Split splits whenever it encounters whitespace by default.
# You can pass the split method a DELIMITER that it will split on.

line = 'first;second;third;fourth'
split_line = line.split(';') # Here ';' is the DELIMITER.
print(split_line) # Prints ['first', 'second', 'third', 'fourth'].