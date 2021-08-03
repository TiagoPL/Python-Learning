from math import cos, sin, tan, radians

ang = float(input('Digite um ângulo: '))
seno = sin(radians(ang))
coseno = cos(radians(ang))
tangente = tan(radians(ang))
print(f'O angulo de {ang} tem o seno de {seno:.2f}.')
print(f'O angulo de {ang} tem o coseno de {coseno:.2f}.')
print(f'O angulo de {ang} tem o tangente de {tangente:.2f}.')
