from utilidadescev import funcoes

p = float(input('Digite o preço: '))
print(f'A metade de {funcoes.moeda(p)} é {funcoes.moeda(funcoes.metade(p))}')
print(f'O dobro de {funcoes.moeda(p)} é {funcoes.moeda(funcoes.dobro(p))}')
print(f'Aumentando 10%, temos {funcoes.moeda(funcoes.aumentar(p))}')
print(f'Reduzindo 13%, temos {funcoes.moeda(funcoes.diminuir(p))}')
