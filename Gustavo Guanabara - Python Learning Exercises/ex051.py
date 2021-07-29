inicio = int(input('Escolha o inicio da PA: '))
razao = int(input('escolha a razao da PA: '))
for cont in range(inicio, inicio + (10 * razao), razao):
    print(cont)
