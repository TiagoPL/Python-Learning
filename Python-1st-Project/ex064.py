n = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero qualquer, ou "999" para parar: '))
    if n != 999:
        soma = soma + n
print(f'O valor da soma dos numeros digitados foi de {soma}.')
