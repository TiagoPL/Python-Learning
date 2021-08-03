from random import choice

print("Let's play Jokenpo!!".center(40, '='))

my_list = ['rock', 'paper', 'scissors']
computer = choice(my_list)
player = str(input('Choose! Rock, Paper or Scissors? ')).lower().strip()

if computer == 'rock':
    print(computer)
    if player == 'rock':
        print(f'The computer played {computer.upper()}!')
        print('Draw!')
    elif player == 'paper':
        print(f'The computer played {computer.upper()}!')
        print('You won!')
    elif player == 'scissors':
        print(f'The computer played {computer.upper()}!')
        print('You lost.')

elif computer == 'paper':
    print(computer)
    if player == 'rock':
        print(f'The computer played {computer.upper()}!')
        print('You lost.')
    elif player == 'paper':
        print(f'The computer played {computer.upper()}!')
        print('Draw!')
    elif player == 'scissors':
        print(f'The computer played {computer.upper()}!')
        print('You won!')

else:
    print(computer)
    if player == 'rock':
        print(f'The computer played {computer.upper()}!')
        print('You Won!')
    elif player == 'paper':
        print(f'The computer played {computer.upper()}!')
        print('You lost.')
    elif player == 'scissors':
        print(f'The computer played {computer.upper()}!')
        print('Draw!')
