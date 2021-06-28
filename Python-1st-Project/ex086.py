lista = [[], [], []]

for cont in range(0, 3):
    lista[0].append(int(input(f'Digite o valor [0, {cont}] da matriz: ')))

for cont in range(0, 3):
    lista[1].append(int(input(f'Digite o valor [1, {cont}] da matriz: ')))

for cont in range(0, 3):
    lista[2].append(int(input(f'Digite o valor [2, {cont}] da matriz: ')))

print(f'''Voce digitou a seguinte matriz:
[{lista[0][0]:^5}][{lista[0][1]:^5}][{lista[0][2]:^5}]
[{lista[1][0]:^5}][{lista[1][1]:^5}][{lista[1][2]:^5}]
[{lista[2][0]:^5}][{lista[2][1]:^5}][{lista[2][2]:^5}]''')
