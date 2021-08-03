my_list1 = []
my_list2 = []
my_list3 = []
answer = 'Y'
while answer == 'Y':
    test = (int(input('Choose a number: ')))
    if test not in my_list1:
        my_list1.append(test)
    answer = input('Do you want to continue? [Y/N]: ').upper()
for c1 in my_list1:
    if c1 % 2 == 0:
        my_list2.append(c1)
    else:
        my_list3.append(c1)
print(f'All entered values: {sorted(my_list1)}.')
print(f'All PAIR values {sorted(my_list2)}.')
print(f'All ODD values {sorted(my_list3)}.')
