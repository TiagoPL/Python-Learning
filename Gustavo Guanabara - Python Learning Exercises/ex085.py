lista = [[], []]
numero = 0

for cont in range(0, 7):
    numero = int(input('Escolha um numero: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

print(f'Os numero pares digitados foram: "{sorted(lista[0])}".')
print(f'Os numeros impares digitados foram: "{sorted(lista[1])}".')
