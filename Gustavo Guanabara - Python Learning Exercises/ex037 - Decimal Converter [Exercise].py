n = int(input('Choose a number: '))
escolha = int(input('''Choose to what format to convert it:
Type 1 for binary
Type 2 for octal
Type 3 for hexadecimal
: '''))
if escolha == 1:
    print(f'The number {n} converted to binary is {bin(n)}')
elif escolha == 2:
    print(f'The number {n} converted to octal is {oct(n)}')
elif escolha == 3:
    print(f'The number {n} converted to hexadecimal is {hex(n)}')
else:
    print("The number you typed isn't valid.")
