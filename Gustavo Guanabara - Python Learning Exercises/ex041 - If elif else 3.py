import datetime
nasc = int(input('Type the year you were born: '))
idade = datetime.date.today().year - nasc
if idade <= 9:
    print(f'{idade} years, category: MIRIM.')
elif idade > 9 and idade <= 14:
    print(f'{idade} years, category: INFANTIL.')
elif idade > 14 and idade <= 19:
    print(f'{idade} years, category: JUNIOR.')
elif idade == 20:
    print(f'{idade} years, category: SENIOR.')
else:
    print(f'{idade} years, category: MASTER.')
