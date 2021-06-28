def contador(inicio, fim, passo):
    for cont in range(inicio, fim, passo):
        print(f'{cont}, ', end='')


# contador(1, 10, 1)
# contador(10, -2, -2)

n1 = int(input('Digite o inicio da contagem: '))
n2 = int(input('Digite o fim da contagem: '))
n3 = int(input('Digite o passo da contagem: '))

print('=' * 40)
if n1 > n2 and n3 > 0:
    print(f'Passo inválido, o valor será invertido de [{n3}] para [{n3 * -1}].')
    n3 = n3 * -1
if n1 < n2 and n3 < 0:
    print(f'Passo inválido, o valor será invertido de [{n3}] para [{n3 * -1}].')
    n3 = n3 * -1
if n3 == 0:
    print(f'Passo inválido, o valor será invertido de [0] para [1].')
    n3 = 0

contador(n1, n2, n3)
