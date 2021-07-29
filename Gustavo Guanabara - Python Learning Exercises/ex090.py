nome = input('Qual o nome do aluno? ')
media = float(input('Qual a média do aluno? '))
if media > 5:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

aluno = {'Nome': nome, 'Media': media, 'Situação': situacao}

print('=' * 40)
print(f'''Nome do aluno: {aluno["Nome"]}
Média do aluno: {aluno["Media"]}
Situação: {aluno["Situação"]}''')
