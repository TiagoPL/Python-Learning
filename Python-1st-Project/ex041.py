import datetime
nasc = int(input('Digite o ano de nascimento: '))
idade = datetime.date.today().year - nasc
if idade <= 9:
    print(f'{idade} anos, categoria MIRIM.')
elif idade > 9 and idade <= 14:
    print(f'{idade} anos, categoria INFANTIL.')
elif idade > 14 and idade <= 19:
    print(f'{idade} anos, categoria JUNIOR.')
elif idade == 20:
    print(f'{idade} anos, categoria SENIOR.')
else:
    print(f'{idade} anos, categoria MASTER.')
