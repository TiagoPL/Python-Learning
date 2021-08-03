import os


# Complete the jumpingOnClouds function below.
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

    return steps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
