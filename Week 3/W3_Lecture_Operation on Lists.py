L = [2,3,4,5,6,7,8]


# Extends list by appending elements from the iterable
L.extend([11,12])


# Extend the list by one object (eg. a list in the original list)
L.append([11,12])


# Delete element at a specific index:
del(L(0))


# Remove element at the end of list, returns the removed element:
L.pop()


# Remove a specific element with L.remove(element)
# - Looks for the element and remove it
# - If element occurs multiple times, removes first occurrence
# - If element not in list, gives an error
L.remove(5)


# Turn the string into a list with its characters as elements
list('asdfdsf')


# Use .split method to split a string on a character parameter, splits on spaces if called
# without a parameter.
s.split()


# Use ''.join(L) to turn a list of characters into a string.
# Can give a character in quotes to add char b/n every element.
''.join(L) # The opposite of s.split()
'__'.join(L)


# Sort a list, but do not mutate it:
sorted(L)


# Sort a list and mutate it (Does not return a value):
L.sort()


# Reverse the order of a list
L.reverse()


# Aliasing a list:
L2 = L


# Cloning a list:
L2 = L[:]
# Or
L2 = L.copy()


"""
Avoid mutating a list as you are iterating over it
- Python uses an internal counter to keep track of index it is in the loop
- Mutating changes the list length but Python doesn't update the counter
- Loop never sees element 2
"""
