import os


# Complete the hourglassSum function below.
def hourglassSum(arr):
    higher = None
    for line in range(0, 4):
        for collum in range(0, 4):
            first_line = arr[line][collum] + arr[line][collum + 1] + arr[line][collum + 2]
            second_line = arr[line + 1][collum + 1]
            third_line = arr[line + 2][collum] + arr[line + 2][collum + 1] + arr[line + 2][collum + 2]
            current = first_line + second_line + third_line
            if higher is None:
                higher = current
            else:
                if current > higher:
                    higher = current
    return higher


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
