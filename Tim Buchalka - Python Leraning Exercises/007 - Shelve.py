import shelve

fruit = shelve.open('ShelfTest')
fruit['Orange'] = 'A sweet, orange, citrus fruit'
fruit['Apple'] = 'Good for making cider'
fruit['Lemon'] = 'A sour, yellow, citrus fruit'
fruit['Grape'] = 'A small, sweet fruit'
fruit['Lime'] = 'A sour, green fruit'

# print(fruit["Lemon"])
# print(fruit["Grape"])

while True:
    dict_key = input('Please enter a fruit: ')
    if dict_key == 'quit':
        break

    if dict_key in fruit:
        description = fruit[dict_key]
        print(description)
    else:
        print('We dont have a ', dict_key)

print('Ordered List: ')
ordered_keys = list(fruit.keys())
ordered_keys.sort()
for f in ordered_keys:
    print(f, '-', fruit[f])

fruit.close()
