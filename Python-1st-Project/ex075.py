n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro: '))
n3 = int(input('Digite mais um: '))
n4 = int(input('Digite o ultimo: '))
lista = (n1, n2, n3, n4)
print(f'O valor "9" apareceu {lista.count(9)} vezes.')
if 3 in lista:
    print(f'O valor "3" apareceu na {lista.index(3) + 1}ª posição.')
else:
    print('O valor "3" não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram: ', end='')
for cont in lista:
    if cont % 2 == 0:
        print(cont, end=' ')
