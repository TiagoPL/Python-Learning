soma = 0
for cont in range(0,6):
    n = int(input('Digite um numero: '))
    if n % 2 == 1:
        soma = soma + n
print(f'A soma dos numeros impares digitados foi {soma}.')
