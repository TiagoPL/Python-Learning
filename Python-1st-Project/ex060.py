noriginal = int(input('Escolha um numero para saber o fatorial: '))
natual = noriginal
nfinal = noriginal
while noriginal != 1:
    natual = natual * (noriginal - 1)
    noriginal = noriginal - 1
print(f'O fatorial de "{nfinal}" é "{natual}".')
