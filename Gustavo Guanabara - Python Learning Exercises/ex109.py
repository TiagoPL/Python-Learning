from utilidadescev import funcoes

p = float(input('Digite o preço: '))
print(f'A metade de {funcoes.moeda(p)} é {funcoes.metade(p, True)}')
print(f'O dobro de {funcoes.moeda(p)} é {funcoes.dobro(p, True)}')
print(f'Aumentando 10%, temos {funcoes.aumentar(p, True)}')
print(f'Reduzindo 13%, temos {funcoes.diminuir(p, True)}')
