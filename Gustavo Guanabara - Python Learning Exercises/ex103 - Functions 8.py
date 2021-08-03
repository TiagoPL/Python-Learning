def stats(name='', scores=0):
    print(f'The player {name} scored {scores} goals in the championship.')


answer = input('Enter player name: ')
if answer == '':
    answer = '<Unknown>'
answer2 = input('Enter the number of goals he scored: ')
if answer2 == '':
    answer2 = 0
stats(answer, answer2)
