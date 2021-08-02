r1 = int(input('Whats the lenght of the 1° line? '))
r2 = int(input('Whats the lenght of the 2° line? '))
r3 = int(input('Whats the lenght of the 3° line? '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Those lines could form a triangle')
    if r1 == r2 == r3:
        print('The triangle would be a equilateral.')
    elif r1 != r2 != r3:
        print(f'The triangle would be a scalene.')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print(f'The triangle would be a isosceles.')
else:
    print("Those lines couldn't form a triangle")
