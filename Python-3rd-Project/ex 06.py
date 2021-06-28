# def rotLeft(a, d):                                   # This way takes too long with big numbers
#     list_copy = []
#     for rotation in range(0, d):
#         for item in range(1, n):
#             list_copy.append(a[item])
#         list_copy.append(a[0])
#         a = list_copy
#         list_copy = []
#
#     return a

def rotLeft(a, d):
    if d > n:
        d = d % n

    list_copy = []
    list_copy.append(a[n - 1])

    for rotations in range(0, d):
        list_copy.append(a[rotations])
    for rest in range(n - 2, d - 1, -1):
        list_copy.insert(0, a[rest])

    return list_copy


n = 10                                 # Tamanho da lista
d = 4                                  # Numero de rotações
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    # Lista

result = rotLeft(a, d)
print(result)
