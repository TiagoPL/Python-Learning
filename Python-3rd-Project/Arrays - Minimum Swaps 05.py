def minimumSwaps(arr):
    reference_arr = sorted(arr)
    index_dict = {valor: index for index, valor in enumerate(arr)}
    swaps = 0

    for index, valor in enumerate(arr):
        correct_value = reference_arr[index]
        if valor != correct_value:
            to_swap_ix = index_dict[correct_value]
            arr[to_swap_ix], arr[index] = arr[index], arr[to_swap_ix]
            index_dict[valor] = to_swap_ix
            index_dict[correct_value] = index
            swaps += 1

    return swaps


arr = [2, 4, 1, 3]
res = minimumSwaps(arr)
print(res)
