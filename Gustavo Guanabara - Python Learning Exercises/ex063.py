t = int(input('Escolha quantos elementos de uma Sequencia de Fibonacci voce quer ver: ')) - 2
n1 = 0
n2 = 1
n3 = 1
print(n1, end=' - ')
print(n2, end=' - ')
while t > 0:
    n3 = n1 + n2
    print(n3, end=' - ')
    n1 = n2
    n2 = n3
    t = t - 1
