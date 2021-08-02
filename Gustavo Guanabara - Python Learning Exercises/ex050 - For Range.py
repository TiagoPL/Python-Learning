result = 0

for cont in range(0, 6):
    n = int(input('Type a number: '))
    if n % 2 == 1:
        result = result + n

print(f'The combined valor of the numbers typed is {result}.')
