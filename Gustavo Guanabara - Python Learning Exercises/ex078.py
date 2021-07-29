lista = []
maior = 0
menor = 0
for cont in range(0, 5):
    lista.append(int(input('Digite um numero: ')))
    if cont == 0:
        maior = lista[cont]
        menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print(f'O maior numero digitado foi {maior} nas posições: ', end='')
for cont2 in range(0, len(lista)):
    if lista[cont2] == maior:
        print(f'{cont2}...', end='')
        print('')
print(f'O menor numero digitado foi {menor} nas posições: ', end='')
for cont3 in range(0, len(lista)):
    if lista[cont3] == menor:
        print(f'{cont3}...', end='')
