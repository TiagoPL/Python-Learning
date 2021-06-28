def makeAnagram(a, b):
    count = 0
    for letter in a:
        if letter not in b:
            new_string = a.replace(letter, '', 1)
            a = new_string
            print(f'{letter} removed')
            count += 1

    print('=' * 60)

    for letter in b:
        if letter not in a:
            new_string = b.replace(letter, '', 1)
            b = new_string
            print(f'{letter} removed')
            count += 1

    print('=' * 60)

    for letter in a:
        if a.count(letter) > b.count(letter):
            new_string = a.replace(letter, '', 1)
            a = new_string
            print(f'{letter} removed Double')
            count += 1

    for letter in b:
        if b.count(letter) > a.count(letter):
            new_string = b.replace(letter, '', 1)
            b = new_string
            print(f'{letter} removed Double')
            count += 1

    print(sorted(a))
    print(sorted(b))
    return count


a = 'fcrxzwscanmligyxyvym'
b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

res = makeAnagram(a, b)
print(res)
