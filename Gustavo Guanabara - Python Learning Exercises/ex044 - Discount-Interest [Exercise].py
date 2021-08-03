price = float(input('How many dollars does the product cost? '))
print("=" * 30)
method = int(input('''Choose payment method:
Cash, TYPE 1
1x on the card, ENTER 2
2x on the card, ENTER 3
3x or more on the card, ENTER 4
: '''))
if method == 1:
    print(f'The product price in cash, with a 10% discount, is {price / 100 * 90:.2f} dollars.')
elif method == 2:
    print(f'The price of the product in 1x on the card, with 5% discount, is {price / 100 * 95:.2f} dollars.')
elif method == 3:
    print(f'The price of the product in 2x on the card, without additions, is {price:.2f} dollars.')
elif method == 4:
    print(f'The price of the product in 3x or more on the card, with 20% interest, is {price / 100 * 120:.2f} dollars')
else:
    print('The number of the chosen option is not valid.')
