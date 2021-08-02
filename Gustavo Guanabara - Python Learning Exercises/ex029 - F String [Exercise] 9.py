v = int(input('Whats the speed of the car? '))
if v < 80:
    print("The car wasn't over the speed limit.")
else:
    print(f'''The car was over the speed limit and will have to pay {(v - 80) *7} bucks, 
    as 7 bucks per km/h over the limit.''')
