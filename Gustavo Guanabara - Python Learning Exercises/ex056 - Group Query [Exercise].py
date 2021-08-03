# average = 0
# older_man = 'ninguem'
# older_man_age = 0
# young_woman = 0
# for cont in range(0, 4):
#     name = input('Digite seu nome: ')
#     age = int(input('Digite sua idade: '))
#     sex = input('Digite seu sexo [M/F]: ').lower().strip()
#     print('=' * 50)
#     average = average + age
#     if age > older_man_age and sex == 'm':
#         older_man = name
#         older_man_age = age
#     if sex == 'f' and age < 20:
#         young_woman = young_woman + 1
# average = average / 4
# print(f'A media da idade do grupo é de {average} anos.')
# print(f'O nome do homem mais velho é {older_man.capitalize()}.')
# print(f'{young_woman} mulheres tem menos de 20 anos.')

average = 0
older_man = ''
older_man_age = 0
young_woman = 0
for count in range(0, 4):
    name = input('Enter your name:')
    age = int(input('Enter your age:'))
    sex = input('Enter your sex [M/F]:') .lower(). strip()
    print('=' * 50)
    average = average + age
    if age > older_man_age and sex == 'm':
        older_man = name
        elderly_man_age = age
    if sex == 'f' and age < 20:
        young_woman = young_woman + 1
average = average / 4
print(f'The average age of the group is {average} years.')
print(f'The oldest man is {older_man.capitalize()}. ')
print(f'{young_woman} womens are under 20.')
