n1 = int(input('Enter a number: '))
n2 = int(input('Type another: '))
n3 = int(input('Enter one more: '))
n4 = int(input('Enter the last: '))
my_list = (n1, n2, n3, n4)
print(f'The value "9" appeared {my_list.count(9)} times.')
if 3 in my_list:
    print(f'The value "3" appeared in {my_list.index(3) + 1}th position.')
else:
    print('The value "3" was not typed in any position')
print(f'The even values entered were: ', end='')
for cont in my_list:
    if cont % 2 == 0:
        print(cont, end=' ')
