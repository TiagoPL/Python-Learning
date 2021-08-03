answer = 'Y'
my_list = []
while answer == 'Y':
    choice = int(input('Enter a number: '))
    if choice not in my_list:
        my_list.append(choice)
        print('Number added to list')
    else:
        print('Repeated number, not added')
    answer = input('Do you want to continue? [Y/N] ').upper()
print(f'The numbers entered were: {sorted(my_list)}')
