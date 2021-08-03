my_list = ('Pencil', 1.75, 'Eraser', 2.00, 'Notebook', 15.90, 'Case', 25.00, 'Drawer', 4.20,
           'Compass', 9.99, 'Backpack', 120.32, 'Pens', 22.30, 'Book', 34.90)
print('=' * 40)
print(f'{"PRICE LISTING":^40}')
print('=' * 40)
for item in range(0, len(my_list)):
    if item % 2 == 0:
        print(f'{my_list[item]:.<30}', end='')
    else:
        print(f'R${my_list[item]:>7.2f}')
print('=' * 40)
