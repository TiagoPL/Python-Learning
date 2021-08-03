higher = 0
smaller = 999
for cont in range(0, 5):
    weight = float(input('Type a Weight: '))
    if weight > higher:
        higher = weight
    elif weight < smaller:
        smaller = weight
print(f'The smallest valor was {smaller}Kg and the highest was {higher}Kg.')
