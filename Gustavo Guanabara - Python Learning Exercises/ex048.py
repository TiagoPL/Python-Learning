soma = 0
for cont in range(1, 501):
    if cont % 3 == 0 and cont % 2 != 0:
        soma = soma + cont
print(soma)
