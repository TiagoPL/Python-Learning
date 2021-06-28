def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n1 = str(input(msg))
        if n1.isdigit():
            valor = int(n1)
            ok = True
        else:
            print('\033[0;31mErro! Digite um numero INTEIRO válido. \033[m')
        if ok:
            break
    return valor


def leiafloat(msg):
    ok = False
    valor = 0
    while True:
        try:
            valor = float(input(msg))
        except:
            print('\033[0;31mErro! Digite um numero REAL válido. \033[m')
        else:
            ok = True
        if ok:
            break
    return valor


nint = leiaint('Digite um número inteiro: ')
nfloat = leiafloat('Digite um numero real: ')

print(f'Voce digitou o numero inteiro {nint}')
print(f'Voce digitou o numero real {nfloat}')
