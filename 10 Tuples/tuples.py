# Tuples function very much like a list. They are 0 indexed, written with () instead of [], you can look-up indexed elements,
# but you cannot alter them - they are immutable (hashable).

new_tuple = () # tuple constructor.

# Tuples take up less storage, quicker to access and are ultimately designed to be more efficient.
# You can convert a tuple into a list using list(tuplename), but there's no point in doing this as if you ever need something
# to be a list, you can just make it a list in the first place.

#  In programming, when making temporary variables we prefer to use tuples as opposed to lists.

# We can put tuples on the left side of an assignment statement. The () are optional.

(x, y) = (4, 'test')
print(y)
print(x)

# You can also return tuples from functions to get multiple variables back from it.

# Tuples are comparable, however they only iterate through a tuple until they find a pair that return a valid true/false value
# from the tuple. Therefore, any following elements are IGNORED.

(0, 1, 2) < (5, 1, 2)
# returns True because 5 is greater than 0 (even though the remaining elements are equal).

('Jones', 'Sally') < ('Jones', 'Sam')
# returns True because in Python l is work less than m (idk why). It ignores the remaining letters in either string.