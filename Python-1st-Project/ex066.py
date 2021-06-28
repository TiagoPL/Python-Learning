cont = 0
n = 0
s = 0
while n != 999:
    n = int(input('Escolha um numero para somar, ou digite [999] para parar: '))
    if n == 999:
        break
    s = s + n
    cont = cont + 1
if cont >= 2:
    print(f'Voce digitou {cont} numeros.')
    print(f'A soma dos numeros digitados é de {s}.')
elif cont == 1:
    print(f'Voce só  digitou 1 numero, "{s}".')
else:
    print('Voce não digitou nenhum numero.')
