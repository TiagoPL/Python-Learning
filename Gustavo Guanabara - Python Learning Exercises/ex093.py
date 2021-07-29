jogador = {}
gols = []
total = 0

jogador['Nome'] = input('Qual o nome do jogador? ')
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for part in range(0, partidas):
    golspartida = int(input(f'Quantos gols {jogador["Nome"]} marcou na {part + 1}° partida? '))
    gols.append(golspartida)
    total = total + golspartida
jogador['Gols'] = gols
jogador['Total'] = total

print('=' * 50)
print(jogador)

print('=' * 50)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('=' * 50)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for part in range(0, partidas):
    print(f'==> Na partida {part + 1}, fez {jogador["Gols"][part]} gols.')
print(f'Foi um total de {total} gols.')
