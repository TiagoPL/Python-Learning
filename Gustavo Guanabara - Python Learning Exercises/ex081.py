lista = []
resp = 'S'
cont = 0
while resp == 'S':
    lista.append(int(input('Escolha um numero: ')))
    resp = input('Deseja continuar? [S/N]: ').upper()
    cont = cont + 1
print(f'Foram digitados {cont} numeros.')
print(f'Os numeros digitados em ordem decrescente foram {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O valor 5 foi digitado.')
else:
    print('O vlaor 5 não foi digitado.')
