def minimumSwaps(arr):
    counter = 0

    for position, number in enumerate(arr):
        if number != arr.index(number) + 1:
            # copy = arr[arr.index(arr.index(number) + 1)]
            #
            # arr[arr.index(arr.index(number) + 1)] = number
            # arr[arr.index(number)] = copy
            correct_position = arr.index(position + 1)
            arr[position], arr[correct_position] = arr[correct_position], arr[position]

            counter += 1

    return counter


n = 4
arr = [4, 3, 1, 2]
res = minimumSwaps(arr)
print(res)

n = 5
arr = [2, 3, 4, 1, 5]
res = minimumSwaps(arr)
print(res)

n = 7
arr = [1, 3, 5, 2, 4, 6, 7]
res = minimumSwaps(arr)
print(res)
