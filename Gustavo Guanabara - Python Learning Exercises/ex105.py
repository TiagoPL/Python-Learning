def notas(* n, sit=True):
    dicionario = {}
    dicionario["Quantidade De Notas"] = len(n)
    dicionario["Maior Nota"] = 0
    dicionario["Menor Nota"] = 999

    for cont in n:
        if cont > dicionario["Maior Nota"]:
            dicionario["Maior Nota"] = cont

    for cont in n:
        if cont < dicionario["Menor Nota"]:
            dicionario["Menor Nota"] = cont

    soma = 0
    for cont2 in n:
        soma = soma + cont2
    media = soma / len(n)
    dicionario["Media"] = float(f'{media:.2f}')

    if sit == True:
        if dicionario["Media"] >= 5:
            dicionario["SITUAÇÃO"] = 'Situação BOA'
        else:
            dicionario["SITUAÇÃO"] = 'Situação RUIM'

    print(dicionario)


notas(4, 5, 6, 7, 1, 9, sit=False)
