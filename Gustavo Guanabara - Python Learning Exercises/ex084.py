lista = []
listatemp = []
resp = 'S'
pessoas = 0
pessoapesada = ['', 0]
pessoaleve = ['', 0]

while resp == 'S':
    print('=' * 50)
    listatemp.append(str(input('Digite um nome: ')))
    listatemp.append(float(input('Digite o peso dessa pessoa: ')))

    if pessoapesada == ['', 0]:
        pessoapesada = listatemp[:]
        pessoaleve = listatemp[:]
    elif listatemp[1] > pessoapesada[1]:
        pessoapesada = listatemp[:]
    elif listatemp[1] < pessoaleve[1]:
        pessoaleve = listatemp[:]

    lista.append(listatemp[:])
    listatemp.clear()
    pessoas = pessoas + 1
    resp = input('Deseja continuar? [S/N]: ').upper().strip()
    while resp != 'S' and resp != 'N':
        resp = input('Deseja continuar? [S/N]: ').upper().strip()

print('=' * 50)
print(f'{pessoas} pessoas foram cadastradas.')
print(f'O maior peso foi de {pessoapesada[1]}Kg. Peso de ', end='')
for cont in lista:
    if cont[1] == pessoapesada[1]:
        print(f'[{cont[0]}] ', end='')
print()
print(f'O menor peso foi de {pessoaleve[1]}Kg. Peso de ', end='')
for cont in lista:
    if cont[1] == pessoaleve[1]:
        print(f'[{cont[0]}] ', end='')
