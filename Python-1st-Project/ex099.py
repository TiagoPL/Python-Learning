from time import sleep


def maior(* n):
    maiornumero = 0
    cont = 0

    print('=' * 40)
    print(f'Os numeros informados foram: ')
    for valor in n:
        print(f'{valor} ', end='')
        if valor > maiornumero:
            maiornumero = valor
        sleep(0.5)
    print()
    print('-' * 40)
    print(f'Foram passados as todo {len(n)} numeros.')
    print(f'O maior numero passado foi {maiornumero}.')
    print('=' * 40)


maior(2, 9, 4, 5, 7, 1)
