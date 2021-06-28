resp = 'S'
maior = 0
homens = 0
menor = 0
cont = 0
while resp == 'S':
    print('=' * 40)
    idade = int(input('Qual a idade da pessoa? '))
    sexo = 'X'
    while sexo != 'M' and sexo != 'F':
        sexo = input('Qual o sexo da pessoa? [M/F]: ').upper().strip()
    if idade > 18:
        maior = maior + 1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        menor = menor + 1
    cont = cont + 1
    resp = input('Deseja cadastrar mais uma pessoa? [S/N]: ').upper().strip()
    while resp != 'S' and resp != 'N':
        resp = input('Deseja cadastrar mais uma pessoa? [S/N]: ').upper().strip()
print('=' * 40)
print(f'''Das {cont}(s) pessoa(s) cadastradas:
{maior} são maiores de 18 anos.
{homens} são homens.
{menor} são mulheres com menos de 20 anos.''')
