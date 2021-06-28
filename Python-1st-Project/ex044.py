preco = float(input('Quantos reais custa o produto? '))
print("=" * 30)
metodo = int(input('''Escolha o meio de pagamento:
A vista no dinheiro, DIGITE 1
A vista no cartão, DIGITE 2
Ate 2x no cartão, DIGITE 3
3x ou mais no cartão, DIGITE 4
: '''))
if metodo == 1:
    print(f'O preco do produto a vista no dinheiro, com 10% de desconto, é {preco / 100 * 90:.2f} reais.')
elif metodo == 2:
    print(f'O preco do produto a vista no cartão, com 5% de desconto, é {preco / 100 * 95:.2f} reais.')
elif metodo == 3:
    print(f'O preco do produto em até 2x no cartão, sem acrécimos, é de {preco:.2f} reais.')
elif metodo == 4:
    print(f'O preco do produto em 3x ou mais no cartão, com 20% de juros, é de {preco / 100 * 120:.2f} reais.')
else:
    print('O numero da opção escolhida não é valida.')
