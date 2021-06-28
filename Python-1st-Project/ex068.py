from random import randint
resultado = 'VITORIA'
while resultado == 'VITORIA':
    print('=' * 60)
    escolha = input('Escolha [PAR] ou [IMPAR]: ').upper().strip()
    jogador = int(input('Escolha um numero entre [0] e [2]: '))
    maquina = randint(0, 2)
    print(f'A maquina jogou [{maquina}]')
    soma = (jogador + maquina)
    if soma % 2 == 0:
        parimpar = 'PAR'
    else:
        parimpar = 'IMPAR'
    if parimpar == escolha:
        print(f'Resultado {soma}. Voce ganhou!')
    else:
        print(f'Resultado {soma}. Voce perdeu.')
        resultado = 'DERROTA'
