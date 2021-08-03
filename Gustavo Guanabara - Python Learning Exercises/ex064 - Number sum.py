n = 0
n_sum = 0
while n != 999:
    n = int(input('Enter any number to add, or "999" to stop: '))
    if n != 999:
        n_sum = n_sum + n
print(f'The sum of the numbers entered was {n_sum}.')
