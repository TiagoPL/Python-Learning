def ficha(nome='', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


resp1 = input('Digite o nome do jogador: ')
if resp1 == '':
    resp1 = '<Desconhecido>'
resp2 = input('Digite o numero de gols que ele fez: ')
if resp2 == '':
    resp2 = 0
ficha(resp1, resp2)
