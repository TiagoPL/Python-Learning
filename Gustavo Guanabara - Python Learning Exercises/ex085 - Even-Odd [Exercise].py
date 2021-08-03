my_list = [[], []]
number = 0

for contain in range(0, 7):
    number = int(input('Choose a number: '))
    if number % 2 == 0:
        my_list[0].append(number)
    else:
        my_list[1].append(number)

print(f'The even numbers entered were: "{sorted(my_list[0])}".')
print(f'The odd numbers entered were: "{sorted(my_list[1])}".')
