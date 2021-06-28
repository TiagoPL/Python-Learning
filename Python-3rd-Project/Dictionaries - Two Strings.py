def twoStrings(s1, s2):
    answer = 'NO'

    for letter in s1:
        for other_letter in s2:
            if other_letter == letter:
                answer = 'YES'
    return answer


s1 = 'hello'
s2 = 'world'
result = twoStrings(s1, s2)
