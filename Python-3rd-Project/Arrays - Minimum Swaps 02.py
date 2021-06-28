def minimumSwaps(arr):
    counter = 0
    arr_dict = {v: i for i, v in enumerate(arr)}

    for position, number in enumerate(arr):
        correct_value = arr.index(number) + 1

        if number != arr.index(number) + 1:
            target_position = arr_dict[(arr.index(number) + 1)]
            arr[target_position], arr[position] = arr[position], arr[target_position]

            arr_dict[number] = target_position
            arr_dict[correct_value] = position

            counter += 1

    return counter


n = 7
arr = [1, 3, 5, 2, 4, 6, 7]

res = minimumSwaps(arr)
print(res)
