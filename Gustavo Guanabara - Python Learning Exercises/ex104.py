def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n1 = str(input(msg))
        if n1.isnumeric():
            valor = int(n1)
            ok = True
        else:
            print('\033[0;31mErro! Digite um numero válido. \033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Voce acabou de digitar o numero {n}')
