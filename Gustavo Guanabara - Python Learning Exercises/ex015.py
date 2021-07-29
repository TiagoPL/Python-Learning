dias = int(input('Quantos dias o carro ficou alugado? '))
dist = int(input('Quantos KM o carro percorreu? '))
print(f'O aluguel do carro seria no valor de {(dias *60) + (dist *0.15):.2f} reais')
