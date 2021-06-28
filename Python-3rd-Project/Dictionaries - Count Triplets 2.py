from collections import Counter


def countTriplets(arr, r):
    arr_dict = Counter(arr)
    counter_dict = Counter()
    answer = 0
    for number in arr:
        j = number // r
        k = number * r
        arr_dict[number] -= 1
        if counter_dict[j] and arr_dict[k] and not number % r:
            answer += counter_dict[j] * arr_dict[k]
        counter_dict[number] += 1
    return answer


n = 4
r = 2
arr = [1, 2, 2, 4]
ns = countTriplets(arr, r)
print(f'Shoud be "2", was "{ns}".')

n = 6
r = 3
arr = [1, 3, 9, 9, 27, 81]
ns = countTriplets(arr, r)
print(f'Shoud be "6", was "{ns}".')

n = 5
r = 5
arr = [1, 5, 5, 25, 125]
ns = countTriplets(arr, r)
print(f'Shoud be "4", was "{ns}".')
