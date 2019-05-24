x = -27
for i in range(abs(x)+1):
    if i**3 >= abs(x):
        break
if i**3 == x:
    print(i, 'is the cube root of', x)
elif i**3*-1 == x:
    print(-i, 'is the perfect cube root of', x)
else:
    print(x, 'is not a perfect cube')

cube = -27
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of '+ str(cube)+ ' is '+ str(guess))
