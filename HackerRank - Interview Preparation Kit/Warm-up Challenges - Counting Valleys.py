import os

# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path


def countingValleys(steps, path):
    answer = 0
    position = 0
    for letter in path:
        if letter == 'U':
            position += 1
        elif letter == "D" and position == 0:
            position -= 1
            answer += 1
        else:
            position -= 1

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
