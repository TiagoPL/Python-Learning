from random import randint
from time import sleep

my_list = []
temp_list = []
number_of_games = int(input('How many games do you wish to simulate? '))
cont = 0

for cont2 in range(0, number_of_games):
    while True:
        number = randint(1, 60)
        if number not in temp_list:
            temp_list.append(number)
            cont = cont + 1
        if cont >= 6:
            break
    my_list.append(temp_list[:])
    temp_list.clear()
    if len(my_list) < number_of_games:
        cont = 0

print('=' * 40)
for cont in range(len(my_list)):
    print(f'{cont + 1}° game sorted: {sorted(my_list[cont])}')
    sleep(1)
