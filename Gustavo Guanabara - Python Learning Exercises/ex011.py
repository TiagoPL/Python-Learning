lar = float(input('Qual a largura da parede em metros? '))
alt = float(input('Qual a altura da parede em metros? '))
area = lar * alt
print(f'''A area dessa parde é de {area:.2f} metros quadrados, e seriam precisos {area /2:.0f} latas de tinta,
assumindo que cada lata pinte 2m².''')
