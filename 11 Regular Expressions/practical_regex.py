 # Regex version of finding hostnames from emails. We've done this with string slicing before.

import re
lin = 'From dave@dave.co.uk Sat Jan 2 02:30:21 2009'
hostname = re.findall('@([^ ]*)', lin) # regex means after @ extract zero or more * non-blank [^ ] chars.
print(hostname) # Prints the item list returned by .findall()

# We can also further fine-tune this by ensuring that it only pulls lines that we want.
# Say for example we only want to extract lines that include 'From'.

import re
lin2 = 'From beanbeans ajhsdkjahskjdhkajsd dave@dave.co.uk Sat Jan 2 02:30:21 2009'
hostname = re.findall('From .*@([^ ]*)', lin2) # Only looks for strings that start with From followed by a space and then any number of chars before an @.
print(hostname)

# Parsing mbox-short.txt to find the maximum X-DSPAM-Confidence value.

print('Parsing mbox-short.txt to find the maximum X-DSPAM-Confidence value.')
import re
fname = input('')
if fname == '' : # Don't forget to use two = signs when comparing. = sets values, == compares to see if they're the same.
    fname = 'mbox-short.txt'
fhandle = open(fname)
dspamlist = []
for line in fhandle :
    line = line.rstrip()
    search = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(search) != 1 : # When I wrote this, I put if search != 1 instead of len(search). We are checking to see if the regex actually returned anything to the list.
        # If the length of the list search != 1 it means nothing was found by .findall().
        continue
    floatsearch = float(search[0]) # Converts the single item in lst(search) to a float. Make sure you don't just put the name of the list. You need to give the index too!
    dspamlist.append(floatsearch) # Which is then appended to the list we'll use to calculate max values.

# print('DEBUG: Printing dspamlist', dspamlist)
print('Maximum:', max(dspamlist)) # Got there in the end.

