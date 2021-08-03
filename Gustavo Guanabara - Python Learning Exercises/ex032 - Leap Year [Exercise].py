a = int(input('Type a Year: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 ==0:
    print(f'Thats a leap year.')
else:
    print(f"That ain't a leap year.")
