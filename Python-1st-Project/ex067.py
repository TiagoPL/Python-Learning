n = 1
while n > 0:
    n = int(input('Escolha um numero para saber a tabuada: '))
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{cont} x {n} = {cont * n}')
print('Voce digitou um numero negativo.')
