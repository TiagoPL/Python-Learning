n = int(input('Escolha um numero: '))
escolha = int(input('''Escolha para oque convertê-lo:
Para BINARIO digite 1
Para OCTAL digite 2
Para HEXADECIMAL digite 3
: '''))
if escolha == 1:
    print(f'O numero {n} convertido para binário é {bin(n)}')
elif escolha == 2:
    print(f'O numero {n} convertido para octal é {oct(n)}')
elif escolha == 3:
    print(f'O numero {n} convertido para hexadecimal é {hex(n)}')
else:
    print('O numero digitado não é uma opção válida.')
