from random import randint


def sorteie(lista):
    for cont in range(0, 5):
        lista.append(randint(0, 10))
    print(f'Os numeros sorteados foram: {sorted(lista)}.')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'A soma dos numeros sorteados vale: {soma}.')


numeros = []
sorteie(numeros)
somapar(numeros)
