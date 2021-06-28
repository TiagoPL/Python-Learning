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


# =======================================================================================================

arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
    ]

result = hourglassSum(arr)
print(f'O resultado deveria ser 19, e foi {result}')

# =======================================================================================================

arr2 = [
    [-1, -1, 0, -9, -2, -2],
    [-2, -1, -6, -8, -2, -5],
    [-1, -1, -1, -2, -3, -4],
    [-1, -9, -2, -4, -4, -5],
    [-7, -3, -3, -2, -9, -9],
    [-1, -3, -1, -2, -4, -5]
    ]

result2 = hourglassSum(arr2)
print(f'O resultado deveria ser -6, e foi {result2}')
