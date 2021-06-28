casa = float(input('Quanto irá custa a casa? '))
salario = float(input('Qual é o seu salaio? '))
anos = float(input('Em quantos anos pretende pagar? '))
meses = anos * 12
parcela = casa / meses
if parcela > (salario / 100) * 30:
    print(f'''O valor da parcela seria de {parcela:.2f} reais, maior que 30% do seu salário de {salario:.2f} reais,
portanto o emprestimo foi negado.''')
else:
    print(f'''O valor da parcela seria de {parcela:.2f} reais, menos que 30% do seu salário de {salario:.2f} reais,
portanto o emprestimo foi aprovado.''')
