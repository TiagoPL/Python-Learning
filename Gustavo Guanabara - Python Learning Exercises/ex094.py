dicionario = {}
lista = []
idade = 0
media = 0
mulheres = []

while True:
    dicionario["Nome"] = input('Nome: ').capitalize().strip()
    while not dicionario["Nome"].isalpha():
        print('\33[0;31mERRO! Por favor digite apenas letras.\33[m')
        dicionario["Nome"] = input('Nome: ').capitalize().strip()
    dicionario["Sexo"] = input('Sexo: [M/F] ').upper().strip()
    while dicionario["Sexo"] != 'M' and dicionario["Sexo"] != 'F':
        print('\33[0;31mErro! Por favor digite apenas [M] ou [F]: \33[m')
        dicionario["Sexo"] = input('Sexo: ').upper().strip()
    if dicionario["Sexo"] == 'F':
        mulheres.append(dicionario["Nome"])
    dicionario["Idade"] = input('Idade: ').strip()
    while not dicionario["Idade"].isnumeric():
        print('\33[0;31mErro! Por favor digite apenas o NÚMERO da idade: \33[m')
        dicionario["Idade"] = input('Idade: ').strip()

    idade = idade + int(dicionario["Idade"])
    lista.append(dicionario.copy())
    dicionario.clear()

    resp = input('Quer continuar? [S/N]: ').upper().strip()
    while resp != 'S' and resp != 'N':
        print('\33[0;31mErro! Por favor digite apenas [S] ou [N]: \33[m')
        resp = input('Quer continuar? [S/N]: ').upper().strip()
    if resp == 'N':
        break

media = (idade / len(lista))

print('=' * 50)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.0f} anos.')
if len(mulheres) > 0:
    print(f'C) As mulheres cadastradas foram {mulheres}')
print(f'D) Lista de pessoas que estão acima da média de idade:')
for pessoa in lista:
    if int((pessoa["Idade"])) > media:
        print(f'Nome: {pessoa["Nome"]}; Sexo: {pessoa["Sexo"]}; Idade: {pessoa["Idade"]}')
print('=' * 50)
