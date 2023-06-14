# This document will cover a key example of using list comprehension to abbrieviate a much longer sorting algorithm.
# The following covers sorting the occurences of words from most to least used.

fhand = open('romeo.txt')
counts = { }
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

lst = [ ] # List constructor. This is a temporary list that we use for the sort.
for key, value in counts.items() : # Forms a tuple of kv's from counts{}   
    newtuple = (value, key) # New tuple with the kv pairs reversed (same order as they are in counts{}).
    lst.append(newtuple) # New data structure created as a list of vk tuples that we can now sort!

lst = sorted(lst, reverse=True) # Sorted function arranging the list in descending order (on account of reverse=True).

for value, key in lst[:10] : # Print the first 10 values in the now sorted list.
    print(key, value)

# While this will print out the values nice and neatly, there's a much quicker way of constructing the new data structure,
# without having to store it in a variable!

c = {'a' : 10, 'b' : 1, 'c' : 22}
print(sorted([(v, k) for k, v in c.items()], reverse = True)) # Here we define the data structure in sorted() instead of having to store it in a new variable. List comprehension!

# [(1, 'b'), (10, 'a'), (22, 'c')]