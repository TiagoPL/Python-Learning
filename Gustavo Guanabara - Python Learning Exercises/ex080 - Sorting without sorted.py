my_list = []
for cont in range(0, 5):
    n = int(input('Type a number: '))
    if cont == 0 or n > my_list[-1]:
        my_list.append(n)
    else:
        pos = 0
        while pos < len(my_list):
            if n <= my_list[pos]:
                my_list.insert(pos, n)
                break
            pos = pos + 1
print(my_list)
