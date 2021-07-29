import datetime

dicionario = {}
dicionario['Nome'] = input('Digite seu nome: ')
dicionario['Idade'] = datetime.date.today().year - (int(input('Digite seu ano de nascimento: ')))
dicionario['Numero da Carteira'] = int(input('Digite sua carteira de trabalho ([0] caso nao tenha): '))
if dicionario['Numero da Carteira'] != 0:
    dicionario['Ano de Contratação'] = int(input('Digite seu ano de contratação: '))
    dicionario['Salario'] = float(input('Digite seu salário: '))
    dicionario['Ano de Aposentadoria'] = datetime.date.today().year + \
                                         (35 - (datetime.date.today().year - dicionario['Ano de Contratação']))

print('=' * 50)
for k, v in dicionario.items():
    print(f'{k} da pessoa: {v}')
