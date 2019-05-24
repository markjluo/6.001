# if g is an approximation to the root, then g-p(g)/p'(g) is a better approximation; where p' is
# a derivative of g

epsilon = 0.001
y = 16.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2)-y)/(2*guess))
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))