dias = int(input('For how many days the car was rented? '))
dist = int(input('How many kilometers the car travelled? '))
print(f'''Assuming the daily coast of the rent is of $60.00 plus 0.15 for km travelled, 
the total rent of the car would be of U${(dias *60) + (dist *0.15):.2f}''')
