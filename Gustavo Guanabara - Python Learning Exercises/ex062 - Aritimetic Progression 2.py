start = int(input('Choose the start of the Aritimetic Progression: '))
rate = int(input('Choose the rate of the Aritimetic Progression: '))
cont = 10
resp = 'y'
while resp == 'y':
    while cont != 0:
        print(start)
        start = start + rate
        cont = cont - 1
    resp = input('Would you like to continue? [y/n]').upper().strip()
    if resp == 'y':
        cont = int(input('How many more numbers would you like to see? '))
