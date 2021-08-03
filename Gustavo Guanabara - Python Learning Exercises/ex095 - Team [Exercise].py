team = []
player = {}
games = []

while True:
    player.clear()
    player['name'] = str(input('Name of the player: '))
    tot = int(input('How many games he played? '))
    for c in range(0, tot):
        games.append(int(input(f'How many games he scored on game {c}? ')))
    player['scores'] = games[:]
    player['total'] = sum(games)
    team.append(player.copy())
    while True:
        answer = str(input('Wanna continue? [Y/N] '))
        if answer in 'YN':
            break
        print('Error, please type Y or N.')
    if answer == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(team):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    search = int(input('Show dates of which player? (999) to cancel): '))
    if search == 999:
        break
    if search >= len(team):
        print(f"Error, there's no player with ID {search}")
    else:
        print(f'Player {team[search]["name"]}: ')
        for i, g in enumerate(team[search]['scores']):
            print(f' On the game {i + 1} scored {g} goals')
    print('-' * 40)
print('Come back soon')
