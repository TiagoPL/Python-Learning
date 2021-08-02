n = int(input('Enter a number: '))
count = 1
answer = input('Would you like to type another [Y/N]? ').upper().strip()
average = n
lesser = n
higher = n
while answer == 'Y':
    n2 = int(input('Enter another number: '))
    count = count + 1
    answer = input('Would you like to type another [Y/N]? ').upper().strip()
    average = (average + n2)
    if n2 < n:
        lesser = n2
    else:
        higher = n2
final_average = average / count
print(f'The average of the values entered was {final_average}.')
print(f'The smallest number entered was {lesser}.')
print(f'The highest number entered was {higher}.')
