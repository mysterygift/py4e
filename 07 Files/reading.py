fhandle = open('loremipsum.rtf', 'r') # Creates a filehandle for loremipseum.rtf in read-mode and stores it in variable fhandle.
count = 0 # Initialises a variable for counting.
for line in fhandle : # For loop that iterates through each line in the file (the filehandle is what gives this that functionality)
    count = count + 1 # Adds to the line count.
print('Line Count:',count) # Prints!

# We can also read entire files (incl newlines) into a single sting using the .read() method. For large files this is not
# recommended as it will store a LOT of information in a new variable.

fhandle = open('loremipsum.rtf') # Creates a filehandle for loremipsum.rtf.
inp = fhandle.read() # Uses read() to store the entire file as a single string variable (inp).
print(len(inp)) # Prints the number of characters in string inp.
print(inp) # Prints the string. Because this is an rtf the first line contains a lot of information about the file format.

# Searching through a file can be done using if statements nested in a for loop.

fhandle = open('loremipsum.rtf')
for line in fhandle :
    if line.startswith('B') : # The startswith() method returns true if the string starts with the argument passed to it.
        print(line)

# OUTPUTS //
# BRITISH!

# BEANS

# BROKEN

# BLAND

# BUTCHER

# //

# The above function prints TWO newlines as the print() function adds a newline in addition to the newline present after each word in the original document.
# We can counter this by using lstrip()/rstrip() to remove whitespace!

fhandle = open('loremipsum.rtf')
for line in fhandle :
    line = line.rstrip() # Removes whitespace from the end of the line.
    if line.startswith('B') or line.startswith('b') : # NB! logical statements are case sensitive. OR >>> or. AND >>> and. &&, || do not work like in C++.
        print(line)

# OUTPUTS //
# BRITISH!
# BEANS
# BROKEN
# BLAND
# BUTCHER
# blue
# barnacle
# //

# We can also use continue and "if not" statements to skip through unwanted data.

fhandle = open('loremipsum.rtf')
for line in fhandle :
    line = line.rstrip()
    if not '{' in line : # This line creates a condition that returns true if a string passed into the itervar 'line' doesn't contain '{'.
        continue # This skips to the next iteration of the loop.
    print(line)

# Obviously we can also pass a variable name into open() in order to allow for user input. This WILL traceback if the file does not exist however.
# ...so be sure to use a try statement.

filefound = 0
while(filefound == 0) :
    fname = input('Please enter a file name: ')
    try :
        fhandle = open(fname)
        filefound = filefound + 1
    except :
        print(f'File {fname} not found/could not be opened. Please try again.')
        continue

    print('File found!\n'+'Processing...\n'+'...\n'+'...\n')
    count = 0
    for line in fhandle :
        if line.startswith('{') :
            count = count + 1
    print(f'There are {count} junk lines in {fname}.')