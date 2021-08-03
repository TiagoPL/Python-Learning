from random import randint
num = randint(0, 9999)
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print(f'''Number chosen {num}.
{m}
{c}
{d}
{u}''')
