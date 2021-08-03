n = int(input('Choose a number: '))
if n % 2 != 0 or n == 1 or n == 2 or n == 3:
    if n % 3 != 0 or n == 1 or n == 2 or n == 3:
        print('Thats a prime number')
    else:
        print('Thats not a prime number')
else:
    print('Thats not a prime number')
