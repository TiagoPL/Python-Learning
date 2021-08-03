s = ''
# while s != 'M' and s != 'F':
while s not in 'MF':
    s = input('Enter your gender [M/F]: ').upper().strip()
if s == 'M':
    print('You typed MALE.')
if s == 'F':
    print('You typed FEMALE.')
