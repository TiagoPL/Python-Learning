from random import randint
n = randint(0, 5)
e = int(input('Escolha um numero entre 0 e 5: '))
if n == e:
    print('Voce acertou!')
else:
    print('Voce errou')
