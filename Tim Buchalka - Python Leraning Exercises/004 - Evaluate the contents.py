lista = 'Batata', 'Astronauta', (3, 'Pão'), (4, 'Cadeira gamer')

with open('/\\Evaluate.txt', 'w') as evaluate_file:
    print(lista, file=evaluate_file)

with open('/\\Evaluate.txt', 'r') as evaluate_file:
    contents = evaluate_file.readline()

final = eval(contents)
print(final)
