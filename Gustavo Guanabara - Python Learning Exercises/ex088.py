from random import randint
from time import sleep

lista = []
listatemp = []
numeroj = int(input('Quantos jogos deseja simular? '))
cont = 0

for cont2 in range(0, numeroj):
    while True:
        numero = randint(1, 60)
        if numero not in listatemp:
            listatemp.append(numero)
            cont = cont + 1
        if cont >= 6:
            break
    lista.append(listatemp[:])
    listatemp.clear()
    if len(lista) < numeroj:
        cont = 0

print('=' * 40)
for cont in range(len(lista)):
    print(f'{cont + 1}° jogo sorteado: {sorted(lista[cont])}')
    sleep(1)
