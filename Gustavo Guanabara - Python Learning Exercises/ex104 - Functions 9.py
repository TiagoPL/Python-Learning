def readint(msg):
    ok = False
    value = 0
    while True:
        n1 = str(input(msg))
        if n1.isnumeric():
            value = int(n1)
            ok = True
        else:
            print('\033[0;31mError! Please enter a valid number. \033[m')
        if ok:
            break
    return value


n = readint('Enter a number: ')
print(f'You just typed the number {n}')
