from random import choice
print('Vamos jogar Jokenpô!!'.center(40, '='))
lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)
jogador = str(input('Escolha! Pedra, Papel ou Tesoura? ')).lower().strip()
if computador == 'pedra':
    if jogador == 'pedra':
        print(f'O computador jogou {computador.upper()}!')
        print('Empate!')
    elif jogador == 'papel':
        print(f'O computador jogou {computador.upper()}!')
        print('Voce ganhou!')
    elif jogador == 'tesoura':
        print(f'O computador jogou {computador.upper()}!')
        print('Voce perdeu.')
elif computador == 'papel':
    if jogador == 'pedra':
        print(f'O computador jogou {computador.upper()}!')
        print('Voce perdeu.')
    elif jogador == 'papel':
        print(f'O computador jogou {computador.upper()}!')
        print('Empate!')
    elif jogador == 'tesoura':
        print(f'O computador jogou {computador.upper()}!')
        print('Voce ganhou!')
elif computador == 'tesoura':
    if jogador == 'pedra':
        print(f'O computador jogou {computador.upper()}!')
        print('Voce Ganhou!')
    elif jogador == 'papel':
        print(f'O computador jogou {computador.upper()}!')
        print('Voce perdeu.')
    elif jogador == 'tesoura':
        print(f'O computador jogou {computador.upper()}!')
        print('Empate!')
