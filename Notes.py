
1.
"""
% is the insertion symbol and it's used for insertion
inside a string, and unlike the coma ( , ) we can insert a value anywhere on the string.
We normally use this in string formatting. Let's see a small example:
"""

celsius = 9
print("%i C = %.2f F"% (celsius, celsius * 1.8 +32))

# The %i inserts an integer, the %f inserts a float,
# we also have %d for double and %s for string.
# The %.2f means only show two decimal spaces.


2.
# Print out the characters of the string s and their indices
s = "Hello World"
for i in range(len(s)):
    print("char = %s index = %i" % (s[i], i))


3.
# Stripping white spaces(characters):

s = " Hello World "
sRightstrip = s.rstrip()
print(sRightstrip)
sLeftstrip = s.lstrip()
print(sLeftstrip)
sStrip = s.strip()
print(sStrip)

# The rstrip() method returns a string with the trailing white space characters removed.
# The lstrip() method returns a string with the leading white space characters removed.
# The strip() method returns a copy of the string with the leading and trailing characters removed.




4.
# Changing cases:

# The upper() method returns a copy of the string where all characters are converted to uppercase.

# The lower() method returns a copy of the string where all characters are converted to lowercase.

# The swapcase() method swaps the case of the letters. Lowercase characters will be uppercase and vice versa.

# The title() method returns a copy of the string, where the first character is in uppercase
# and the remaining characters are in lowercase.


5.
"""
Advanced slicing:

When you only include one colon, you are indicating the start and end steps. For example, in "hello"[1:3] 1 is 
the start index and 3 is the end index.

When you include two colons, you are indicating that you want to "skip" the end parameter, located in the middle, 
and use the default value for end, which is the end of the string.Then, you set a value for the third 
parameter (step). For example, "hello"[1::3] means that start is 1, end is the end of the string, 
the default value, and step is 3.
"""

a = 'hello'
print(a[::-1])
print(a[:-1])



5.

# a += b is equivalent to a = a + b

# a -= b is equivalent to a = a - b

# a *= b is equivalent to a = a * b

# a /= b is equivalent to a = a / b



6.
# Generate integers from 5 to 1.
for i in range(5, 0, -1):
    print(i)
# Generate even integers from 0 to 4
for i in range(0, 5, 2):
    print(i)

7.
# Decomposition: Break problem into different, self-contained, pieces.
# Decomposition with functions and classes.

# Abstraction: Suppress details of method to compute something from use of that computation.
# Achieve abstraction with function specifications or docstrings.


8.
# Returned functions

def add(x, y):
    return x + y

def multiply(x, y):
    return x*y

def addormultiply(a):
    if a > 5:
        return add
    else:
        return multiply

# Execute returned function immediately: Use two parenthesis
addormultiply(6)(5,10)

# Store function returned in a variable:
add = addormultiply(6)
multiply = addormultiple(4)

add(5, 10)
multiply(5, 10)


9.
# Recursion:
# - A way to design solutions to problems by divide-and-conquer or decrease-and-
# conquer
# - A programming technique where a function calls itself

# - Each recursive call to a function creates its own scope/environment
# - Bindings of variables in a scope is not changed by recursive call
# - Flow of control passes back to previous scope conce function call returns value
