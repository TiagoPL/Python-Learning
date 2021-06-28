resp = 'S'
lista = []
while resp == 'S':
    escolha = int(input('Digite um numero: '))
    if escolha not in lista:
        lista.append(escolha)
        print('Numero adicionado a lista')
    else:
        print('Numero repetido, não adicionado')
    resp = input('Deseja continuar? [S/N] ').upper()
print(f'Os numeros digitados foram: {sorted(lista)}')
