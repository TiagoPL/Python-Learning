def repeatedString(s, n):
    a_in_string = 0
    total_a = 0
    for letter in s:
        if letter == 'a':
            a_in_string += 1

    clean_ones = n // len(s)
    clean_add = clean_ones * a_in_string
    total_a += clean_add

    letters_left = n % len(s)
    for letter in range(0, letters_left):
        if s[letter] == 'a':
            total_a += 1

    return total_a


# ===============================================================================================

s = 'aba'
n = 10

result = repeatedString(s, n)
print(result)

s = 'a'
n = 1000000000000

result = repeatedString(s, n)
print(result)

s = 'gfcaaaecbg'
n = 547602

result = repeatedString(s, n)
print(result)

s = 'aab'
n = 882787

result = repeatedString(s, n)
print(result)
