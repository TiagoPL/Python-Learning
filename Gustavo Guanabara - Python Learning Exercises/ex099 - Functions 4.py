from time import sleep


def higher(* n):
    high_number = 0
    print('=' * 40)
    print(f'The numbers chosen were: ')
    for value in n:
        print(f'{value} ', end='')
        if value > high_number:
            high_number = value
        sleep(0.5)
    print()
    print('-' * 40)
    print(f'{len(n)} numbers were given.')
    print(f'The highest number was {high_number}.')
    print('=' * 40)


higher(2, 9, 4, 5, 7, 1)
