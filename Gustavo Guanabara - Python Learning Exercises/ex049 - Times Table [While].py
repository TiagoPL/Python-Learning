n1 = int(input('Type a number to see its times table: '))
cont = 1

while True:
    print(f'{n1} x {cont} = {n1 * cont}')
    cont += 1
    if cont > 10:
        break
