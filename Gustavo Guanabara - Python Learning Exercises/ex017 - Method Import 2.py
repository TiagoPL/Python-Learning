from math import hypot

cat1 = float(input('Whats the size of the Opposite side ? '))
cat2 = float(input('Whats the size of the Adjacent side? '))
# cat1s = cat1 ** 2
# cat2s = cat2 ** 2
# hips = cat1s + cat2s
# hip = hips ** 0.5
hip = hypot(cat1, cat2)
print(f'The hypotenuse size is {hip:.2f}.')
