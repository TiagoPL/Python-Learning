import datetime
maior = 0
menor = 0
for cont in range(0, 7):
    ano = int(input('Type a year someone was born: '))
    if datetime.date.today().year - ano >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'{maior} of them are over 18, {menor} arent.')
