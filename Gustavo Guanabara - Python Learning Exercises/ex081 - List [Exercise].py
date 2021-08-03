my_list = []
answer = 'Y'
counter = 0
while answer == 'Y':
    my_list.append(int(input('Pick a number: ')))
    answer = input('Do you want to continue? [Y/N]: ').upper()
    counter = counter + 1
print(f'You typed {counter} numbers.')
print(f'The numbers entered in descending order were {sorted(my_list, reverse=True)}')
if 5 in my_list:
    print(f'The value 5 has been entered.')
else:
    print('Vlaor 5 has not been typed.')
