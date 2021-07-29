n = int(input('Escolha um numero: '))
if n % 2 != 0 or n == 1 or n == 2 or n == 3:
    if n % 3 != 0 or n == 1 or n == 2 or n == 3:
        print('Esse numero é primo')
    else:
        print('Esse numero não é primo')
else:
    print('Esse numero não é primo')
