nome = input('Type your full name: ').strip().title()
lista = nome.split()
print(f'Nice to meet you, {lista[0]}!')
print(f'your last name is {lista[len(lista)-1]} right?')
