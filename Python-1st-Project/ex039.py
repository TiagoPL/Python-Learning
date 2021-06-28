import datetime
ano = int(input('Em que ano voce nasceu? '))
data = datetime.date.today().year
if ano < 2003:
    print(f'Voce tem {data - ano} anos e já deveria ter se alistado.')
elif ano == 2003:
    print(f'Voce tem {data - ano} anos e precisa se alistar.')
else:
    print(f'Voce tem {data - ano} anos e ainda não precisa se alistar.')
