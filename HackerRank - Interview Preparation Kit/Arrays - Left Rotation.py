def rotLeft(a, d):
    temp_list = []

    if d > len(a):
        d = d % len(a)

    for item in range(0, d):
        temp_list.append(a[item])

    for item in range(0, d):
        a.pop(0)

    for item in temp_list:
        a.append(item)

    return a


d = 4
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = rotLeft(a, d)
print(result)

d = 34
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = rotLeft(a, d)
print(result)
