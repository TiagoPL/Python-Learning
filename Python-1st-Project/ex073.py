lista = ('São Paulo', 'Internacional', 'Atlético Mineiro', 'Flamengo', 'Gremio', 'Palmeiras', 'Fluminense',
         'Santos', 'Ceará', 'Corinthians', 'Atlético-PR', 'Atlético Goianiense', 'Bragantino', 'Sport Recife',
         'Vasco da Gama', 'Fortaleza', 'Bahia', 'Goiás', 'Botafogo', 'Coritiba')
print(f'Os 5 primeiros colocados do brasileirão são {lista[:5]}.')
print(f'Os ultimos 4 colocados do brasileirão são {lista[-4:]}')
print(f'Os times em ordem alfabética são {sorted(lista)}')
print(f'O time Palmeiras está na {lista.index("Palmeiras") + 1}° posição.')
