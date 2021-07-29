s = ''
while s != 'M' and s != 'F':
    s = input('Digite seu sexo [M/F]: ').upper().strip()
if s == 'M':
    print('Você digitou MASCULINO.')
if s == 'F':
    print('Voce digitou FEMININO.')
