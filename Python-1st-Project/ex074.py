from random import randint
lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os numeros gerados foram {sorted(lista)}')
print(f'O menor valor gerado foi {min(lista)}.')
print(f'O maior valor gerado foi {max(lista)}.')
