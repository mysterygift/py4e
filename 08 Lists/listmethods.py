# Python comes with a number of methods that can be used on this. These can be recapped using the dir function.
t = ['a', 'b', 'c']
type(t) # <class 'list'>
dir(t) # This lists all the methods available to 't', which is a list. You can also find these using dir(list).

# These include append, count, extend, index, insert, pop, remove, reverse, sort and more.
# Note that [] in pop, index indicate OPTIONAL parameters.

# .append(x) – adds a specified object x to the end of a list.
# .count(x) - returns the number of times x appears in a list.
# .extend(x) - extends the list by appending elements from an iteranle.
    # x = [1, 2, 3]
    # x.extend([4, 5])
    # print(x)
    # [1, 2, 3, 4, 5]
# .index(x) - returns a zero-based index in the list from the first item equal to x.
    # .index(x[, start[, end]]) - start/end correspond with slice notation that can limit the range searched.
# .insert(i, x) - inserts item x before position i.
# .pop([i]) - removes and returns the item at position i. If not item is specified, it removes and returns the last item.
# .remove(x) - removes the first item in the list that is equal to x.
# .reverse(x) - reverses the order of the list.
# .sort(*, key=None, reverse=False) - sorts items of the list in ascending order.
    # Because lists are mutable they can be sorted in place - you don't need to assign them to a new variable (unlike strings).

# Write a program that allows users to input numbers until they enter 'done', and output the average.

numlist = list() # Constructor sets up an empty list.
PLAYERSTATE = True # I kept using == here instead of =. STUPID! It works now.
while(PLAYERSTATE == True) : # Infinite loop.
    inp = input('Enter a number: ') 
    if (inp == 'done') or (inp == 'Done') : # Checks to see if user is finished.
        PLAYERSTATE = False
    else :
        float_inp = float(inp) # As we will be calculating averages, need to user floating point.
        numlist.append(float_inp) # Adds floating point value to the end of the list.

average = sum(numlist) / len(numlist)
print('Average:',average) # Comma automatically adds a space.