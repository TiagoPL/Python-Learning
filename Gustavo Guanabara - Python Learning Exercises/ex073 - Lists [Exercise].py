my_list = ('São Paulo', 'International', 'Atlético Mineiro', 'Flamengo', 'Gremio', 'Palmeiras', 'Fluminense',
           'Santos', 'Ceará', 'Corinthians', 'Atlético-PR', 'Atlético Goianiense', 'Bragantino', 'Sport Recife',
           'Vasco da Gama', 'Fortaleza', 'Bahia', 'Goiás', 'Botafogo', 'Coritiba')
print(f'The top 5 of the brazillian championship are {my_list[:5]}.')
print(f'The last 4 places are {my_list[-4:]}')
print(f'The teams in alphabetical order are {sorted(my_list)}')
print(f'The "Palmeiras" team is on {my_list.index("Palmeiras") + 1}th position.')
