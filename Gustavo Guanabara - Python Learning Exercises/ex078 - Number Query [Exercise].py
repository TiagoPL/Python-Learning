my_list = []
higher = 0
lesser = 0
for counter1 in range(0, 5):
    my_list.append(int(input('Enter a number: ')))
    if counter1 == 0:
        higher = my_list[counter1]
        lesser = my_list[counter1]
    else:
        if my_list[counter1] > higher:
            higher = my_list[counter1]
        if my_list[counter1] < lesser:
            lesser = my_list[counter1]
print(f'The highest number entered was {higher} in the position: ', end='')
for counter2 in range(0, len(my_list)):
    if my_list[counter2] == higher:
        print(f'{counter2 + 1}°', end='')
        print('')
print(f'The smallest number entered was {lesser} in the position: ', end='')
for counter3 in range(0, len(my_list)):
    if my_list[counter3] == lesser:
        print(f'{counter3 + 1}°', end='')
