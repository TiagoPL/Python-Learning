import datetime
maior = 0
menor = 0
for cont in range(0, 7):
    ano = int(input('Digite seu ano de nascimento: '))
    if datetime.date.today().year - ano >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'{maior} pessoas já chegaram na maioridade e {menor} pessoas ainda não.')
