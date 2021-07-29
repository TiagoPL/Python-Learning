def twoStrings(s1, s2):
    s1 = set(s1)
    s2 = set(s2)

    for letter in s1:
        for other_letter in s2:
            if other_letter == letter:
                return 'YES'

    return 'NO'


s1 = 'hello'
s2 = 'world'
result = twoStrings(s1, s2)
