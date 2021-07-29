n1 = 0
n2 = 0
escolha = 4
maior = n1
while escolha != 5:
    while escolha == 4:
        print('=' * 50)
        n1 = int(input('Escolha um numero: '))
        n2 = int(input('Escolha outro numero: '))
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('=' * 45)
        print('Oque deseja fazer com os numeros digitados?')
        print('[1] para somá-los.')
        print('[2] para multiplicálos.')
        print('[3] para saber o maior.')
        print('[4] para escolher novos numeros.')
        print('[5] para sair do programa.')
        escolha = int(input(''))
        if escolha == 1:
            print(f'A soma dos valores digitados é {n1 + n2}.')
        elif escolha == 2:
            print(f'O produto dos numeros digitados é {n1 * n2}')
        elif escolha == 3:
            print(f'O maior entre os numeros digitados foi {maior}')
