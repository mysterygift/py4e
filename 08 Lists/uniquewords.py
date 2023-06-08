# Find all unique words within a file and output them in alphabetical order.

uniquewords = list()
word_buffer = list() # Buffer list to load each line into once it has been split().
state = 0 # Variable for the while loop that contains the program to ensure that it will only quit when the user enters a valid filename.
while state < 1 :
    try :
        filename = input('Enter filename: ')
        fhandle = open(filename)
        state = 1 # If no exception is thrown by this point, state will set to 1, stopping the loop.
        print(f'DEBUG: File', filename, 'successfully opened, state var set to 1.') # For debug.
        for line in fhandle :
            line = line.rstrip() # Just to be safe.
            # print(line)
            word_buffer = line.split()
            # print(word_buffer)
            for word in word_buffer : # Iterates through the buffer to check each word.
                if word not in uniquewords : # Checks if each word has been stored already.
                    uniquewords.append(word) # Appends the uniquewords list if so.
        
        uniquewords.sort() # Alphabetical sort (lowest to highest value).
        print(uniquewords, f'There are', len(uniquewords), 'unique words in this file.')
        # len(x) here counts the number of elements present in the list, as opposed to .count() which
        # returns the number of iterations of a specific element.

    except :
        print(f'File', filename, 'not found. Please try again.') # God I love f-strings.