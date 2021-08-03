from random import randint
my_list = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'The numbers generated were {sorted(my_list)}')
print(f'The smallest value generated was {min(my_list)}.')
print(f'The highest value generated was {max(my_list)}.')
