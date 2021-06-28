def alternatingCharacters(s):
    counter = 0
    for position, letter in enumerate(s):
        try:
            if letter == s[(position + 1)]:
                counter += 1
        except IndexError:
            pass
    return counter


s = 'AAAA'
result = alternatingCharacters(s)
print(result)

s = 'BBBBB'
result = alternatingCharacters(s)
print(result)

s = 'ABABABAB'
result = alternatingCharacters(s)
print(result)

s = 'BABABA'
result = alternatingCharacters(s)
print(result)

s = 'AAABBB'
result = alternatingCharacters(s)
print(result)
