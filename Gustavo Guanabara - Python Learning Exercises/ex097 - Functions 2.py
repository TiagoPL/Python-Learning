def write(txt):
    print('=' * (len(txt) + 4))
    print(f' {txt}')
    print('=' * (len(txt) + 4))


sentence = input(f'Enter the sentence you want to format: ')
write(sentence)
