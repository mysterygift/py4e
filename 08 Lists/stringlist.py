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

# Write code that parses mbox-short.txt and outputs the emails + a count of all the lines that start with 'From'.

fhandle = open('mbox-short.txt', 'r')
email_list = list()
mailcount = 0
for line in fhandle :
    line.rstrip()
    if line.startswith('From:') :
        email_list.append(line[1])
        mailcount = mailcount + 1
    else :
        continue