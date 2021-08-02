n1 = 0
n2 = 0
choice = 4
high_number = n1
while choice != 5:
    while choice == 4:
        print('=' * 50)
        n1 = int(input('Choose a number: '))
        n2 = int(input('Choose another number: '))
        if n1 > n2:
            high_number = n1
        else:
            high_number = n2
        print('=' * 45)
        print('What do you want to do with the numbers?')
        print('[1] to add them up.')
        print('[2] to multiply them.')
        print('[3] to find the higher number.')
        print('[4] to choose new numbers.')
        print('[5] nothing, quit the program.')
        choice = int(input(''))
        if choice == 1:
            print(f'The sum of the entered values is {n1 + n2}.')
            choice = 5
        elif choice == 2:
            print(f'The product of the numbers entered is {n1 * n2}')
            choice = 5
        elif choice == 3:
            print(f'The higher number entered was {high_number}')
            choice = 5
