media = 0
hvelho = 'ninguem'
hvelhoidade = 0
mjovem = 0
for cont in range(0, 4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo [M/F]: ').lower().strip()
    print('=' * 50)
    media = media + idade
    if idade > hvelhoidade and sexo == 'm':
        hvelho = nome
        hvelhoidade = idade
    if sexo == 'f' and idade < 20:
        mjovem = mjovem + 1
media = media / 4
print(f'A media da idade do grupo é de {media} anos.')
print(f'O nome do homem mais velho é {hvelho.capitalize()}.')
print(f'{mjovem} mulheres tem menos de 20 anos.')
