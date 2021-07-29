v = int(input('Qual a velocidade do carro ? '))
if v < 80:
    print('Voce não passou do limite de velocidade.')
else:
    print(f'Voce passou do limite de velocidade e pagara uma multa de {(v - 80) *7} reais.')
