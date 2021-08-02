s = int(input('Whats your salary? '))
if s > 1250:
    print(f'Your new salary, with a 10% bonus will be of {(s /100) * 110 :.2f} dollars.')
else:
    print(f'Your new salary, with a 15% bonus will be of {(s /100) * 115 :.2f} dollars.')
