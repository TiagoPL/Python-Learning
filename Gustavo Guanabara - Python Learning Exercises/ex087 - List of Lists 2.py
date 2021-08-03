# my_list = [[], [], []]
# sum_of_evens = 0
# sum_of_third = 0
# higher_of_second = 0
#
# for cont in range(0, 3):
#     my_list[0].append(int(input(f'Digite o valor [0, {cont}] da matriz: ')))
#     if my_list[0][-1] % 2 == 0:
#         sum_of_evens = sum_of_evens + my_list[0][-1]
#
# for cont in range(0, 3):
#     my_list[1].append(int(input(f'Digite o valor [1, {cont}] da matriz: ')))
#     if my_list[1][-1] % 2 == 0:
#         sum_of_evens = sum_of_evens + my_list[1][-1]
#     if my_list[1][-1] > higher_of_second:
#         higher_of_second = my_list[1][-1]
#
# for cont in range(0, 3):
#     my_list[2].append(int(input(f'Digite o valor [2, {cont}] da matriz: ')))
#     if my_list[2][-1] % 2 == 0:
#         sum_of_evens = sum_of_evens + my_list[2][-1]
#
# sum_of_third = my_list[0][2] + my_list[1][2] + my_list[2][2]
#
# print(f'''Voce digitou a seguinte matriz:
# [{my_list[0][0]:^5}][{my_list[0][1]:^5}][{my_list[0][2]:^5}]
# [{my_list[1][0]:^5}][{my_list[1][1]:^5}][{my_list[1][2]:^5}]
# [{my_list[2][0]:^5}][{my_list[2][1]:^5}][{my_list[2][2]:^5}]''')
#
# print(f'A soma dos numeros pares digitados vale {sum_of_evens}.')
# print(f'A soma dos valores da terceira coluna vale {sum_of_third}.')
# print(f'O maior valor digitado na segunda linha foi {higher_of_second}.')

my_list = [[], [], []]
sum_of_evens = 0
sum_of_third = 0
higher_of_second = 0

for count in range(0, 3):
    my_list[0].append(int(input(f'Enter the value [0, {count}] of the array: ')))
    if my_list[0][-1] % 2 == 0:
        sum_of_evens = sum_of_evens + my_list[0][-1]

for count in range(0, 3):
    my_list[1].append(int(input(f'Enter the value [1, {count}] of the array: ')))
    if my_list[1][-1] % 2 == 0:
        sum_of_evens = sum_of_evens + my_list[1][-1]
    if my_list[1][-1] > higher_of_second:
        higher_of_second = my_list[1][-1]

for count in range(0, 3):
    my_list[2].append(int(input(f'Enter the value [2, {count}] of the array: ')))
    if my_list[2][-1] % 2 == 0:
        sum_of_evens = sum_of_evens + my_list[2][-1]

sum_of_third = my_list[0][2] + my_list[1][2] + my_list[2][2]

print(f'''You typed the following array:
[{my_list[0][0]:^5}][{my_list[0][1]:^5}][{my_list[0][2]:^5}]
[{my_list[1][0]:^5}][{my_list[1][1]:^5}][{my_list[1][2]:^5}]
[{my_list[2][0]:^5}][{my_list[2][1]:^5}][{my_list[2][2]:^5}]''')

print(f'The sum of the even numbers entered is {sum_of_evens}.')
print(f'The sum of the values in the third column is {sum_of_third}.')
print(f'The highest value entered on the second line was {higher_of_second}.')
