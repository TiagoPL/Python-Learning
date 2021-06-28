n1 = int(input('Escolha um numero: '))
n2 = int(input('Escolha outro numero: '))
if n1 > n2:
    print(f'O primeiro numero, "{n1}", é maior do que o segundo, "{n2}".')
elif n1 < n2:
    print(f'O segundo numero, "{n2}", é maior do que o primeiro, "{n1}".')
else:
    print('Ambos os numero são iguais.')
