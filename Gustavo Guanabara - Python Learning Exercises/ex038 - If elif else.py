n1 = int(input('Choose a number: '))
n2 = int(input('Choose a second one: '))
if n1 > n2:
    print(f'The first number, "{n1}", is higher than the second, "{n2}".')
elif n1 < n2:
    print(f'The second number, "{n2}", is higher than the first, "{n1}".')
else:
    print('Both the numbers are the same.')
