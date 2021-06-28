n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'Media {media}, aluno reprovado.')
elif media >= 5 and media < 6.99:
    print(f'Media {media}, aluno em recuperação.')
else:
    print(f'Media {media}, aluno aprovado.')
