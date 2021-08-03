import shelve

blt = ['bacon', 'lettuce', 'tomato', 'bread']
beans_on_toast = ['beans', 'bread']
scrambled_eggs = ['eggs', 'butter', 'milk']
soup = ['tin of soup']
pasta = ['pasta', 'cheese']

with shelve.open('recipes') as recipes:
    recipes['blt'] = blt
    recipes['beans and toast'] = beans_on_toast
    recipes['scrambled eggs'] = scrambled_eggs
    recipes['pasta'] = pasta
    recipes['soup'] = soup

    temp_list = recipes['blt']       # How to append itens in a shelve
    temp_list.append('butter')
    recipes['blt'] = temp_list

    for snack in recipes:
        print(snack, recipes[snack])
