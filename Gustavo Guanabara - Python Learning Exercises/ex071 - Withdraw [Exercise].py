print('=-=' * 15)
value = int(input('Enter the amount you want to withdraw: $'))
if value < 10:
    print(f'Will get:'
          f'{value} bills of $1.00')
elif value < 20:
    print(f'Will get:'
          f'{value // 10} bills of $10.00')
    if value % 10 != 0:
        print(f'{value %10} bills of $1.00')
elif value < 50:
    print(f'''will get:
    {value // 20} bills of $20.00''')
    if value % 20 != 0:
        print(f'''{value // 20} $10.00 bills
    {(value %20) %10} bills of $1.00''')
elif value > 50:
    print(f'''will get:
{value // 50} bills of $50.00''')
    if value % 50 != 0:
        print(f'''{(value %50) // 20} $20.00 bills''')
        if (value % 50) % 20 != 0:
            print(f'''{((value % 50) % 20) // 10} $10.00 bills
{(value %50) %20% 10} bills of $1.00''')
