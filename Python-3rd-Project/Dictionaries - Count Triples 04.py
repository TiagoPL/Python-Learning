def countTriplets(array, ratio):
    answer = 0
    dictionary = {}
    dictionary_pairs = {}

    for number in reversed(array):
        if number * ratio in dictionary_pairs:
            answer += dictionary_pairs[number * ratio]

        if number * ratio in dictionary:
            dictionary_pairs[number] = dictionary_pairs.get(number, 0) + dictionary[number * ratio]

        dictionary[number] = dictionary.get(number, 0) + 1

    return answer


r = 2
arr = [1, 2, 2, 4]
ns = countTriplets(arr, r)
print(f'Shoud be "2", was "{ns}".')

r = 3
arr = [1, 3, 9, 9, 27, 81]
ns = countTriplets(arr, r)
print(f'Shoud be "6", was "{ns}".')

r = 5
arr = [1, 5, 5, 25, 125]
ns = countTriplets(arr, r)
print(f'Shoud be "4", was "{ns}".')
