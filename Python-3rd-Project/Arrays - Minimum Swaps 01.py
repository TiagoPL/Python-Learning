def minimumSwaps(arr):
    counter = 0
    arr_dict = {valor: index for valor, index in enumerate(arr)}

    for position, number in enumerate(arr):
        if number != arr.index(number) + 1:
            # target_position = arr_dict[arr.index(position + 1)]
            # target_position = arr.index(position + 1)
            target_position = arr_dict[(arr.index(number) + 1)]
            arr[target_position], arr[position] = arr[position], arr[target_position]

            print(arr)
            arr_dict[number] = target_position
            print(arr)
            print('=' * 60)

            counter += 1

    return counter


n = 7
arr = [1, 3, 5, 2, 4, 6, 7]

res = minimumSwaps(arr)
print(res)
