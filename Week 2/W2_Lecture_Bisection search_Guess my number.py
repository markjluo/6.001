a= int(input('Please think of a number between 0 and 100: '))
high = 100
low = 0
x = int((high + low)/2)
print('Is your secret number', x, '?')
b = input("Enter 'h' to indicate the guess is too high. "
          "Enter 'l' to indicate the guess is too low. "
          "Enter 'c' to indicate I guessed correctly: ")

while True:
    if b == 'c':
        break
    elif b == 'h':
        high = x
        x = int((high + low)/2)
        print('Is your secret number', x, '?')
        b = input("Enter 'h' to indicate the guess is too high. "
                  "Enter 'l' to indicate the guess is too low. "
                  "Enter 'c' to indicate I guessed correctly: ")
    elif b == 'l':
        low = x
        x = int((high + low)/2)
        print('Is your secret number', x, '?')
        b = input("Enter 'h' to indicate the guess is too high. "
                  "Enter 'l' to indicate the guess is too low. "
                  "Enter 'c' to indicate I guessed correctly: ")
    else:
        print('Sorry, I did not understand your input.')
        print('Is your secret number', x, '?')
        b = input("Enter 'h' to indicate the guess is too high. "
                  "Enter 'l' to indicate the guess is too low. "
                  "Enter 'c' to indicate I guessed correctly: ")

print('Game Over, Your secret number was:', x)