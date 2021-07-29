palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'progrmador', 'futuro')
for cont in range(len(palavras)):
    print(f'Na palavra {palavras[cont].upper()} temos as vogais: ', end='')
    for cont2 in range(len(palavras[cont])):
        ltr = ((palavras[cont])[cont2]).upper()
        if ltr == 'A' or ltr == 'E' or ltr == 'I' or ltr == 'O' or ltr == 'U':
            print(ltr, end='')
    print('')
