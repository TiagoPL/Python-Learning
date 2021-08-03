my_list = [[], [], []]

for cont in range(0, 3):
    my_list[0].append(int(input(f'Enter the value [0, {cont}] of the array: ')))

for cont in range(0, 3):
    my_list[1].append(int(input(f'Enter the value [1, {cont}] of the array: ')))

for cont in range(0, 3):
    my_list[2].append(int(input(f'Enter the value [2, {cont}] of the array: ')))

print(f'''You typed the following array:
[{my_list[0][0]:^5}][{my_list[0][1]:^5}][{my_list[0][2]:^5}]
[{my_list[1][0]:^5}][{my_list[1][1]:^5}][{my_list[1][2]:^5}]
[{my_list[2][0]:^5}][{my_list[2][1]:^5}][{my_list[2][2]:^5}]''')
