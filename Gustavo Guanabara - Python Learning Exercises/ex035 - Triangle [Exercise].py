r1 = int(input('Type the lenght of a line: '))
r2 = int(input('Type one more: '))
r3 = int(input('And one last line: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Those lines CAN form a triangle')
else:
    print('Those lines CANNOT form a triangle')
