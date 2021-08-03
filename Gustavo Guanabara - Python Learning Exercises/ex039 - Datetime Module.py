import datetime
ano = int(input('In which year you was born? '))
data = datetime.date.today().year

print(f'You have {data - ano} years')

# if ano < 2003:
#     print(f'You have {data - ano} anos e já deveria ter se alistado.')
# elif ano == 2003:
#     print(f'Voce tem {data - ano} anos e precisa se alistar.')
# else:
#     print(f'Voce tem {data - ano} anos e ainda não precisa se alistar.')
