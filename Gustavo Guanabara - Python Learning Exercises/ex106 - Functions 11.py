def readint(msg):
    ok = False
    value = 0
    while True:
        n1 = str(input(msg))
        if n1.isdigit():
            value = int(n1)
            ok = True
        else:
            print('\033[0;31mError! Please enter a valid INTEGER number. \033[m')
        if ok:
            break
    return value


def readfloat(msg):
    ok = False
    value = 0
    while True:
        try:
            value = float(input(msg))
        except TypeError:
            print('\033[0;31mError! Please enter a valid REAL number. \033[m')
        else:
            ok = True
        if ok:
            break
    return value


nint = readint('Enter an integer: ')
nfloat = readfloat('Enter a number: ')

print(f'You typed the integer {nint}')
print(f'You typed the number {nfloat}')
