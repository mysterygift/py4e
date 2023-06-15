# Write a function in python that mimics grep from unix.
# This will ask the user to define the path of the file being searched relative to pygrep.py.
# Arguments:
#   Will try as a void function first.
# Need to wrap regex and search to catch the exception. Use state < 2.

def pygrep() :
    import re
    state = 0
    while state < 1 :
        try :
            fname = input('Please enter the file-path of the search file relative to pygrep.py: ')
            fhandle = open(fname)
            state = 1
            counter = 0
        except:
            print(f'File {fname} not found. Please try again.\n')

    
    regex = input('Enter a regular expression to search this file with: ')
    for line in fhandle :
        line.rstrip()
        bufferList = re.findall(f'{regex}', line) # I forgot to make this an f-string. This works!
        if len(bufferList) != 1 :
            continue
        counter += 1
    
    if counter == 0 :
        print(f'{fname} had no lines that matched the regular expression {regex}')
    else :
        print(f'{fname} had {counter} lines that matches {regex}')

        return counter
# pygrep()