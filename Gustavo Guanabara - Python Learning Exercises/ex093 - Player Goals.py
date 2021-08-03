player = {}
scores = []
total = 0

player['Name'] = input("What's the player's name?")
matches = int(input(f'How many matches {player["Name"]} played? '))
for part in range(0, matches):
    match_scores = int(input(f'How many goals did {player["Name"]} scored in the {part + 1}th game? '))
    scores.append(match_scores)
    total = total + match_scores
player['scores'] = scores
player['total'] = total

print('=' * 50)
print(player)

print('=' * 50)
for k, v in player.items():
    print(f'The field {k} has the value {v}.')

print('=' * 50)
print(f'The player {player["Name"]} played {matches} matches.')
for part in range(0, matches):
    print(f'==> In the match {part + 1}, he scored {player["scores"][part]} goal(s).')
print(f'It was a total of {total} goal(s).')
