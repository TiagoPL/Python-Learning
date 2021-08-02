from random import randint

result = 'WIN'
while result == 'WIN':
    print('=' * 60)
    choice = input('Choose [EVEN] or [ODD]: ').upper().strip()
    player = int(input('Choose a number between [0] and [2]: '))
    machine = randint(0, 2)
    print(f'The machine threw [{machine}]')
    number_sum = (player + machine)
    if number_sum % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'
    if odd_even == choice:
        print(f'Result {number_sum}. You won!')
    else:
        print(f'Result {number_sum}. You lost.')
        result = 'DEFEAT'
