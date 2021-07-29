r1 = int(input('Qual o comprimento da primeira reta? '))
r2 = int(input('Qual o comprimento da segunda reta? '))
r3 = int(input('Qual o comprimento da terceira reta? '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas PODEM formar um triangulo')
else:
    print('Essas retas NAO PODEM formar um triangulo')
