casa = float(input('How mush does the house cost? '))
salario = float(input('Whats your salary? '))
anos = float(input('In how many years you plan to pay it? '))
meses = anos * 12
parcela = casa / meses
if parcela > (salario / 100) * 30:
    print(f'''The monthly installment would be of {parcela:.2f} dollars, higher than 30% of your salary of {salario:.2f}
     dollars, therefore the loan was denied.''')
else:
    print(f'''The monthly installment would be of {parcela:.2f} dollars, less than 30% of your salary of {salario:.2f}
         dollars, therefore the loan was approved.''')
