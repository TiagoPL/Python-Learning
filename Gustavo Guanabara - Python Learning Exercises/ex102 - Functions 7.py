def factorial(n1=1, answer=False):
    n2 = n1
    for cont in range(n1 - 1, 0, -1):
        n1 = n1 * cont
    if answer == False:
        print(n1)
    else:
        print(n2, end='')
        for cont2 in range(n2 - 1, 0, -1):
            print(f' * {cont2}', end='')
        print(f' = {n1}')


factorial(4, True)
