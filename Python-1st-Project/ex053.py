frase = input('Digite uma frase: ').upper().strip()
frase = frase.replace(' ', '')
inverso = ''
for cont in range(len(frase) - 1, -1, -1):
    inverso = inverso + frase[cont]
if frase == inverso:
    print('Temos um palindromo.')
else:
    print('Não temos um palindromo.')
