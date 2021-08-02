count = 0
n = 0
s = 0
while n != 999:
    n = int(input('Choose a number to add, or type [999] to stop: '))
    if n == 999:
        break
    s = s + n
    count = count + 1
if count >= 2:
    print(f'You typed {count} numbers.')
    print(f'The sum of the numbers entered is {s}.')
elif count == 1:
    print(f'You only typed 1 number, "{s}".')
else:
    print('You didnt type any number.')
