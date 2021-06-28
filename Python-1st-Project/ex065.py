n = int(input('Digite um numero: '))
cont = 1
resp = input('Gostaria de digitar outro [S/N]? ').upper().strip()
mediainicio = n
menor = n
maior = n
while resp == 'S':
    n2 = int(input('Digite outro numero: '))
    cont = cont + 1
    resp = input('Gostaria de digitar outro [S/N]? ').upper().strip()
    mediainicio = (mediainicio + n2)
    if n2 < n:
        menor = n2
    else:
        maior = n2
mediafinal = mediainicio / cont
print(f'A média dos valores digitados foi {mediafinal}.')
print(f'O menor numero digitado foi {menor}.')
print(f'O maior numero digitado foi {maior}.')
