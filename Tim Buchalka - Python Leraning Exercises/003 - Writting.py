cities = ['Ouro Fino', 'Monte Sião', 'Pouso Alegre', 'Jacutinga',
          'Aguas de Lindóia']

with open('Cities.txt', 'w') as city_file:
    for city in cities:
        print(city, file=city_file)

# ==================================================================

citieslist = []
with open('Cities.txt') as city_file:
    for city in city_file:
        citieslist.append(city)

for city in citieslist:
    print(city, end='')
