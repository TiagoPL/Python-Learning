from random import randint


def raffle(my_list):
    for contains in range(0, 5):
        my_list.append(randint(0, 10))
    print(f'The numbers drawn were: {sorted(my_list)}.')


def add_evens(my_list):
    my_sum = 0
    for value in my_list:
        if value % 2 == 0:
            my_sum = my_sum + value
    print(f'The sum of the numbers drawn is: {my_sum}.')


numbers = []
raffle(numbers)
add_evens(numbers)
