from random import randint
n = randint(0, 10)
e = 11
t = 0
while e != n:
    e = int(input('Choose a number between 0 and 10: '))
    t = t + 1
    if n == e:
        print(f'You got it right! It took you {t} attempts.')
    else:
        print('Wrong guess, try again!')
