def minimumSwaps(arr):
    counter = 0
    to_swap = 0
    dictionary = {key: valor for key, valor in enumerate(arr)}

    for key, value in dictionary.items():
        if value != key + 1:
            print(f'As value "{value}" is in position "{key + 1}":')
            for key2, value2 in dictionary.items():
                if value2 == key + 1:
                    to_swap = key2
                    break

            print(f'List now:   {list(dictionary.values())}')
            print(f'Gonna swap: {dictionary[key]} and {dictionary[to_swap]}')

            copy = dictionary[key]
            dictionary[key] = key + 1
            dictionary[to_swap] = copy

            print(f'Result:     {list(dictionary.values())}')
            print('=' * 60)

            counter += 1
    return counter


n = 7
arr = [1, 3, 5, 2, 4, 6, 7]

res = minimumSwaps(arr)
print(f'Number of swaps: {res}')
