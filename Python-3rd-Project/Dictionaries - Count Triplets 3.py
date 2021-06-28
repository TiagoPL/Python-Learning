def countTriplets(arr, r):
    answer = 0

    for position, number in enumerate(arr):
        for second_position, second_number in enumerate(arr[position + 1:]):
            if number * r == second_number:
                for third_position, third_number in enumerate(arr[second_position + 1:]):
                    if second_number * r == third_number:
                        answer += 1

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
