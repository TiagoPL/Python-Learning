from random import randint
n = randint(0, 5)
e = int(input('Choose a number between 0 and 5: '))
if n == e:
    print('You got it right!')
else:
    print('More luck next time.')
