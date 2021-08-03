from random import choice

s1 = input('Name of the 1° student: ')
s2 = input('Name of the 2° student: ')
s3 = input('Name of the 3° student: ')
s4 = input('Name of the 4° student: ')
lista = [s1, s2, s3, s4]
print(f'The student randomly choosed was: {choice(lista)}')
