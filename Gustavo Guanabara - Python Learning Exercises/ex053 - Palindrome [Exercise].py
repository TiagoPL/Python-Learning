frase = input('Type a phrase: ').upper().strip()
frase = frase.replace(' ', '')
inverso = ''
for cont in range(len(frase) - 1, -1, -1):
    inverso = inverso + frase[cont]
if frase == inverso:
    print('thats a palindrome.')
else:
    print('thats not a palindrome.')
