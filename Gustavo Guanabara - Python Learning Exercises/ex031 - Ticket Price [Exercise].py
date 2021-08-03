d = int(input('Whats the distance in KM? '))
if d < 200:
    print(f'The price of the ticket will be {d * 0.50 :.2f} bucks.')
else:
    print(f'The price of the ticket will be {d * 0.45 :.2f} bucks.')
