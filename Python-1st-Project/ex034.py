s = int(input('Qual o seu salário? '))
if s > 1250:
    print(f'Seu novo salário, com aumento de 10%, será de {(s /100) * 110 :.2f} reais.')
else:
    print(f'Seu novo salário, com aumento de 15%, será de {(s /100) * 115 :.2f} reais.')
