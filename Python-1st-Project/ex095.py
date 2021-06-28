# Código não finalizado. Com problemas.

time = []
jogador = {}
gols = []
total = 0

while True:
    jogador.clear()
    jogador['Nome'] = input('Qual o nome do jogador? ')
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for part in range(0, partidas):
        golspartida = input(f'Quantos gols {jogador["Nome"]} marcou na {part + 1}° partida? ')
        gols.append(golspartida[:])
        total = total + int(golspartida)
    jogador['Gols'] = gols
    jogador['Total'] = total
    time.append(jogador.copy())
    resp = input('Quer continuar? [S/N]: ').upper().strip()
    if resp == 'N':
        break

print('=' * 50)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
        print()
