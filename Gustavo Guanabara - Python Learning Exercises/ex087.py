lista = [[], [], []]
somapares = 0
somaterceira = 0
maiorsegunda = 0

for cont in range(0, 3):
    lista[0].append(int(input(f'Digite o valor [0, {cont}] da matriz: ')))
    if lista[0][-1] % 2 == 0:
        somapares = somapares + lista[0][-1]

for cont in range(0, 3):
    lista[1].append(int(input(f'Digite o valor [1, {cont}] da matriz: ')))
    if lista[1][-1] % 2 == 0:
        somapares = somapares + lista[1][-1]
    if lista[1][-1] > maiorsegunda:
        maiorsegunda = lista[1][-1]

for cont in range(0, 3):
    lista[2].append(int(input(f'Digite o valor [2, {cont}] da matriz: ')))
    if lista[2][-1] % 2 == 0:
        somapares = somapares + lista[2][-1]

somaterceira = lista[0][2] + lista[1][2] + lista[2][2]

print(f'''Voce digitou a seguinte matriz:
[{lista[0][0]:^5}][{lista[0][1]:^5}][{lista[0][2]:^5}]
[{lista[1][0]:^5}][{lista[1][1]:^5}][{lista[1][2]:^5}]
[{lista[2][0]:^5}][{lista[2][1]:^5}][{lista[2][2]:^5}]''')

print(f'A soma dos numeros pares digitados vale {somapares}.')
print(f'A soma dos valores da terceira coluna vale {somaterceira}.')
print(f'O maior valor digitado na segunda linha foi {maiorsegunda}.')
