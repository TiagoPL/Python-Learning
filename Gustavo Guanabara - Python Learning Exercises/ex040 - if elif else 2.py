n1 = float(input('Type the first score: '))
n2 = float(input('Type the second: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'Average {media}, student failed.')
elif media >= 5 and media < 6.99:
    print(f'Average {media}, student needs supplementary lessons.')
else:
    print(f'Average {media}, student aproved.')
