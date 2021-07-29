lista = []
listatemp = []
resp = 'S'
nalunos = 0

while resp == 'S':
    print('=' * 40)
    listatemp.append(input('Nome: ').title())
    listatemp.append(float(input('Nota 1: ')))
    listatemp.append(float(input('Nota 2: ')))
    lista.append(listatemp[:])
    listatemp.clear()
    nalunos = nalunos + 1
    resp = input('Deseja continuar? [S/N]: ').upper().strip()
    if resp != 'S' and resp != 'N':
        while resp != 'S' and resp != 'N':
            resp = input('Comando inválido.'
                         'Deseja continuar? [S/N]: ').upper().strip()

print('=' * 40)
print('N° Nome        Media')
print('-' * 40)
for cont in range(nalunos):
    print(f'{cont:<3}', end='')
    print(f'{lista[cont][0]:<13}', end='')
    print(f'{(lista[cont][1] + lista[cont][2]) / 2}')
print('-' * 40)

while True:
    resp2 = int(input('Ver as notas de qual aluno? [999 interrompe]: '))
    if resp2 == 999:
        break
    else:
        print(f'As notas de {lista[resp2][0]} são {lista[resp2][1], lista[resp2][2]}.')
