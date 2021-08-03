# my_list = []
# temp_list = []
# answer = 'S'
# number_of_students = 0
#
# while answer == 'S':
#     print('=' * 40)
#     temp_list.append(input('Nome: ').title())
#     temp_list.append(float(input('Nota 1: ')))
#     temp_list.append(float(input('Nota 2: ')))
#     my_list.append(temp_list[:])
#     temp_list.clear()
#     number_of_students = number_of_students + 1
#     answer = input('Deseja continuar? [S/N]: ').upper().strip()
#     if answer != 'S' and answer != 'N':
#         while answer != 'S' and answer != 'N':
#             answer = input('Comando inválido.'
#                            'Deseja continuar? [S/N]: ').upper().strip()
#
# print('=' * 40)
# print('N° Nome        Media')
# print('-' * 40)
# for cont in range(number_of_students):
#     print(f'{cont:<3}', end='')
#     print(f'{my_list[cont][0]:<13}', end='')
#     print(f'{(my_list[cont][1] + my_list[cont][2]) / 2}')
# print('-' * 40)
#
# while True:
#     resp2 = int(input('Ver as notas de qual aluno? [999 interrompe]: '))
#     if resp2 == 999:
#         break
#     else:
#         print(f'As notas de {my_list[resp2][0]} são {my_list[resp2][1], my_list[resp2][2]}.')

my_list = []
temp_list = []
answer = 'Y'
number_of_students = 0

while answer == 'Y':
    print('=' * 40)
    temp_list.append(input('Name: ').title())
    temp_list.append(float(input('Score 1: ')))
    temp_list.append(float(input('Score 2: ')))
    my_list.append(temp_list[:])
    temp_list.clear()
    number_of_students = number_of_students + 1
    answer = input('Do you want to continue? [Y/N]: ').upper().strip()
    if answer != 'Y' and answer != 'N':
        while answer != 'Y' and answer != 'N':
            answer = input('Invalid command.'
                           'Do you wish to continue? [Y/N]: ').upper().strip()

print('=' * 40)
print('Media Name No.')
print('-' * 40)
for count in range(number_of_students):
    print(f'{count:<3}', end='')
    print(f'{my_list[count][0]:<13}', end='')
    print(f'{(my_list[count][1] + my_list[count][2]) / 2}')
print('-' * 40)

while True:
    answer2 = int(input('See which student ID grades? [999 interrupt]: '))
    if answer2 == 999:
        break
    else:
        print(f'The notes of {my_list[answer2][0]} are {my_list[answer2][1], my_list[answer2][2]}.')
