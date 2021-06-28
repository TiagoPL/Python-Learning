from math import hypot

cat1 = float(input('Qual o valor do cateto oposto ? '))
cat2 = float(input('Qual o valor do cateto adjacente? '))
#cat1s = cat1 ** 2
#cat2s = cat2 ** 2
#hips = cat1s + cat2s
#hip = hips ** 0.5
hip = hypot(cat1, cat2)
print(f'A valor da hipotenuza é de {hip:.2f}.')
