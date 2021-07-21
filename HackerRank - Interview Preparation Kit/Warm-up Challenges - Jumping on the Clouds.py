def jumpingOnClouds(c):
    steps = 0
    position = 0

    while position < len(c) - 1:
        try:
            if c[position + 2] == 0:
                position += 2
                steps += 1
            else:
                position += 1
                steps += 1
        except IndexError:
            position += 1
            steps += 1
            pass

    return steps


c = [0, 0, 1, 0, 0, 1, 0]
print('Should be 4, was: ', end='')
print(jumpingOnClouds(c))

c = [0, 0, 0, 0, 1, 0]
print('Should be 3, was: ', end='')
print(jumpingOnClouds(c))
