result = 0

for cont in range(1, 501):
    if cont % 3 == 0 and cont % 2 != 0:
        result = result + cont

print(result)
