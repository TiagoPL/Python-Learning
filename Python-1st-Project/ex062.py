inicio = int(input('Escolha o inicio da PA: '))
razao = int(input('Escolha a razao da PA: '))
cont = 10
resp = 'S'
while resp == 'S':
    while cont != 0:
        print(inicio)
        inicio = inicio + razao
        cont = cont - 1
    resp = input('Gostaria de continuar [S/N]? ').upper().strip()
    if resp == 'S':
        cont = int(input('Quantos termos a mais voce quer ver? '))
