def countTriplets(array, ratio):
    pass


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
