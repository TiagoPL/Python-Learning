lista1 = []
lista2 = []
lista3 = []
resp = 'S'
while resp == 'S':
    teste = (int(input('Escolha um numero: ')))
    if teste not in lista1:
        lista1.append(teste)
    resp = input('Deseja continuar? [S/N]: ').upper()
for cont1 in lista1:
    if cont1 % 2 == 0:
        lista2.append(cont1)
    else:
        lista3.append(cont1)
print(f'Todos os valores digitados: {sorted(lista1)}.')
print(f'Todos os valores PARES {sorted(lista2)}.')
print(f'Todos os valores IMPARES {sorted(lista3)}.')
