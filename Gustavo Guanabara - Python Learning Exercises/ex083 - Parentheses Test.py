my_list = []
answer = input('Enter your expression: ')
for cont in range(0, len(answer)):
    my_list.append(answer[cont])
pa = my_list.count('(')
pf = my_list.count(')')
if pa == pf:
    print('This is a valid expression.')
else:
    print('This is NOT a valid expression.')

# Program does not work if parentheses are in the wrong order
