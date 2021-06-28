from random import randint
n = randint(0, 10)
e = 11
t = 0
while e != n:
    e = int(input('Escolha um numero entre 0 e 10: '))
    t = t + 1
    if n == e:
        print(f'Voce acertou! Foram nessesárias {t} tentativas.')
    else:
        print('Voce errou, tente novamente!')
