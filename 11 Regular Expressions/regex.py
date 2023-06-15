# Regular expressions or regex/regexp, provide a concise and flexible means
# to match strings, such as particular chars, words, or patterns of chars.
# Regex can be quite brittle code if you aren't specific enough with your search criteria (as in it breaks if data inputted deviates from a predicted format).

# A regexp can be written in a formal language that can be interpreted by a regular expression processor.
# Using them you can do smart searching/extraction.

# REGULAR EXPRESSION QUICK GUIDE! <<<<
# ^ - Matches the beginning of a line
# $ - Matches the end of the line
# . - Matches any character
# \s - Matches whitespace
# \S - Matches any non-whitespace character
# * - Repeats a character zero or more times
# *? - Repeats a character zero or more times (non-greedy)
# + - Repeats a character one or more times
# +? - Repeats a character one or more times (non-greedy)
# [aeoiu] - Matches a single char in the listed set
# [^XYZ] - Matches a single char NOT in the listed set
# [a-z0-9] - The set of chars can incl a range
# ( - Indicates where a string extraction starts
# ) - Where a string extraction ends
# \ - Escape character. Put this before a special regex char to look for one. e.g. \$ will look for $'s.

# You can use import re to bring in the regexp library.
# re.search() checks if a string matches a regexp, similar to .find() for strings.
# re.findall() extracts portions of a str that matches a regexp, similar to find() and slicing : var[5:10].

import re # import the regular expressions lib

fname = input('Enter file name: ')
if fname == '' :
    fname = 'mbox-short.txt'
fhandle = open(fname)
for line in fhandle :
    line = line.rstrip()
    if re.search('From:', line) : # checks to see if the pattern 'From:' can be found in any line
        print(line) # Outputs the entire line


# Now let's try the same thing but using regexp to mirror the functionality of .startswith().

import re

fname2 = input("Let's do that again: ")
if fname2 == '' :
    fname2 = 'mbox-short.txt'
fhandle2 = open(fname2)
print('\n\n')
for line in fhandle2 :
    line = line.rstrip()
    if re.search('^From: ', line) :
        print(line)

# . matches any char, and if you add a * it means 'any number of times'.
# For example: ^X.*: <- starts with X, followed by zero or more of any char followed by a colon.

import re

fname3 = input("Now to find the X's: ")
if fname3 == '' :
    fname3 = 'mbox-short.txt'
fhandle3 = open(fname3)
print('\n\n')
for line in fhandle3 :
    line = line.rstrip()
    if re.search('^X.*: ', line) :
        print(line)

# We can further refine our search.
# ^X-\S+: Means 'starts with X, until a non-whitespace char one or more times followed by a :.
# This will omit any lines with whitespace before the :.

# MATCHING & EXTRACTING DATA

# re.findall() extracts all matching strings into a list.

print('\nFinding and extracting data using REGEX.')
import re
x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
print(type(y))

# Anything within a [] in REGEX is considered one character.
# Here, [0-9]+ means one or more digits between 0-9.
# Hence, the above function prints ['2', '19', '42']

# * and + push outward in both directions (greedy) to match the largest possible str.
print('\nGreedy Matching')
import re
x = 'From: Using the : char'
y = re.findall('^F.+:', x)
print(y)

# This returns 'From: Using the :'. It has returned the largest possible string that satisfies the condition.
# We can curb this behaviour by adding a ? onto the end of the regexp.

# re.findall('^F.+?', x) would return 'From:'

# We can further fine-tune extraction using parenthesis - which aren't part of the match but indicate where to start and stop.

print('\nFine tuning with ()')
z = [] # List constructor.
print('List z initialised.')
fhandle4 = open('mbox-short.txt', 'r')
for line in fhandle4 :
    line = line.rstrip()
    if re.findall('^From: (\S+@\S+)', line) :
        z.append(line)

print(z)