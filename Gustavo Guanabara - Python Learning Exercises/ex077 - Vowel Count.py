words = ('learn', 'program', 'language', 'python',
         'course', 'free', 'study', 'practice',
         'work', 'market', 'programmer', 'future')
for c in range(len(words)):
    print(f'In the word {words[c].upper()} we have the vowels: ', end='')
    for c2 in range(len(words[c])):
        ltr = ((words[c])[c2]).upper()
        if ltr == 'A' or ltr == 'E' or ltr == 'I' or ltr == 'O' or ltr == 'U':
            print(ltr, end='')
    print('')
