def escreva(txt):
    print('=' * (len(txt) + 4))
    print(f'  {txt}')
    print('=' * (len(txt) + 4))


frase = input(f'Digite a frase que deseja formatar: ')
escreva(frase)
