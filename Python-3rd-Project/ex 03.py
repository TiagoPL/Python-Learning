#!/bin/python3

n = 7


def jumpingOnClouds(c):
    position = 0
    steps = 0
    sky = iter(c)

    for cloud in sky:

        try:
            if c[position + 2] == 0:
                position += 2
                steps += 1
                next(sky)

            else:
                position += 1
                steps += 1

        except IndexError:
            if position < n - 1:
                position += 1
                steps += 1

        print(f'Position: {position}', end='\t')
        print(f'Cloud: {cloud}', end='\t')
        print(f'Steps taken: {steps}')

    return steps


result = jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
print(result)
