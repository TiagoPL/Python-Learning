total = 0
count1000 = 0
name_cheaper = ''
cheaper_price = 999999
answer = 'Y'
while answer == 'Y':
    name = input('What is the name of the product?')
    price = float(input('What is the price of this product in $?'))
    total = total + price
    if price > 1000:
        count1000 = count1000 + 1
    if price < cheaper_price:
        name_cheaper = name
    answer = input('Do you want to register another product? [Y/N]: ').upper()
    print('=' * 40)
print(f'The total spent was R${total:.2f}.')
print(f'{count1000} products cost more than R$1000.00 reais.')
print(f'The cheapest product was {name_cheaper}.')
