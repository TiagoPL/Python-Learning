print('=-=' * 15)
valor = int(input('Digite o valor que quer sacar: R$'))
if valor < 10:
    print(f'Serão retiradas:'
          f'{valor} cédulas de R$1.00')
elif valor < 20:
    print(f'Serão retiradas:'
          f'{valor // 10} cédulas de R$10.00')
    if valor % 10 != 0:
        print(f'{valor % 10} cédulas de R$1.00')
elif valor < 50:
    print(f'''Serão retiradas:
    {valor // 20} cédulas de R$20.00''')
    if valor % 20 != 0:
        print(f'''{valor // 20} cédulas de R$10.00
    {(valor % 20) % 10} cédulas de R$1.00''')
elif valor > 50:
    print(f'''Serão retiradas:  
{valor // 50} cédulas de R$50.00''')
    if valor % 50 != 0:
        print(f'''{(valor % 50) // 20} cédulas de R$20.00''')
        if (valor % 50) % 20 != 0:
            print(f'''{((valor % 50) % 20) // 10} cédulas de R$10.00
{(valor % 50) % 20 % 10} cédulas de R$1.00''')
