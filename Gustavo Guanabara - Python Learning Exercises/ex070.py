total = 0
cont1000 = 0
nomebarato = ''
precobarato = 999999
resp = 'S'
while resp == 'S':
    nome = input('Qual o nome do produto? ')
    preco = float(input('Qual o preco desse produto em R$? '))
    total = total + preco
    if preco > 1000:
        cont1000 = cont1000 + 1
    if preco < precobarato:
        nomebarato = nome
    resp = input('Deseja cadastrar outro produto? [S/N]: ').upper()
    print('=' * 40)
print(f'O total gasto foi de R${total:.2f}.')
print(f'{cont1000} produtos custaram mais de R$1000,00 reais.')
print(f'O produto mais barato foi {nomebarato}.')
