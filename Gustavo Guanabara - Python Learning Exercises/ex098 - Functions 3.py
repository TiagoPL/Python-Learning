def counter(start, end, step):
    for count in range(start, end, step):
        print(f'{count}, ', end='')


# counter(1, 10, 1)
# counter(10, -2, -2)

n1 = int(input('Enter count start: '))
n2 = int(input('Enter the end of count: '))
n3 = int(input('Enter count rate: '))

print('=' * 40)
if n1 > n2 and n3 > 0:
    print(f'Invalid rate, value will be inverted from [{n3}] to [{n3 * -1}].')
    n3 = n3 * -1
if n1 < n2 and n3 < 0:
    print(f'Invalid rate, value will be inverted from [{n3}] to [{n3 * -1}].')
    n3 = n3 * -1
if n3 == 0:
    print(f'Invalid rate, value will be inverted from [0] to [1].')
    n3 = 0

counter(n1, n2, n3)
