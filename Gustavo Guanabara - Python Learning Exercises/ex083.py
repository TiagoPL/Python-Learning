lista = []
resp = input('Digite sua expressão: ')
for cont in range(0, len(resp)):
    lista.append(resp[cont])
pa = lista.count('(')
pf = lista.count(')')
if pa == pf:
    print('Essa é uma expressão válida.')
else:
    print('Essa NAO é uma expressão válida.')

# Programa não funciona se os parenteses estiverem na ordem errada
