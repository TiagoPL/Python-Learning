maior = 0
menor = 999
for cont in range(0, 5):
    peso = float(input('Qual o seu peso? '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O menor peso digitado foi {menor}Kg e o maior foi {maior}Kg.')
