n = 1
while n > 0:
    n = int(input('Choose a number to get the multiplication table: '))
    if n < 0:
        break
    for count in range(1, 11):
        print(f'{count} x {n} = {count * n}')
print('You entered a negative number.')
