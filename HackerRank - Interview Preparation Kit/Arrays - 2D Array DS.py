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


arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
    ]

print(f' Should be 19, was {hourglassSum(arr)}')
