d = int(input('Qual a distancia da viagem em kilometros? '))
if d < 200:
    print(f'O preco da passagem será de {d * 0.50 :.2f} reais.')
else:
    print(f'O preco da passagem será de {d * 0.45 :.2f} reais.')
