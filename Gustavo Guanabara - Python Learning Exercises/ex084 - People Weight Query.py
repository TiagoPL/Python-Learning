my_list = []
temp_list = []
answer = 'Y'
people = 0
heavy = ['', 0]
light = ['', 0]

while answer == 'Y':
    print('=' * 50)
    temp_list.append(str(input('Enter a name: ')))
    temp_list.append(float(input('Enter the weight of this person: ')))

    if heavy == ['', 0]:
        heavy = temp_list[:]
        light = temp_list[:]
    elif temp_list[1] > heavy[1]:
        heavy = temp_list[:]
    elif temp_list[1] < light[1]:
        light = temp_list[:]

    my_list.append(temp_list[:])
    temp_list.clear()
    people = people + 1
    answer = input('Do you want to continue? [Y/N]: ').upper().strip()
    while answer != 'Y' and answer != 'N':
        answer = input('Do you want to continue? [Y/N]: ').upper().strip()

print('=' * 50)
print(f'{people} people have been registered.')
print(f'The highest weight was {heavy[1]}Kg. Weight of ', end='')
for cont in my_list:
    if cont[1] == heavy[1]:
        print(f'[{cont[0]}] ', end='')
print()
print(f'Lesser weight was {light[1]}Kg. Weight of ', end='')
for cont in my_list:
    if cont[1] == light[1]:
        print(f'[{cont[0]}] ', end='')
