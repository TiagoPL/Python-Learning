def repeatedString(s, n):
    a_in_s = s.counter1('a')
    number_of_strings = n // len(s)
    number_of_a = number_of_strings * a_in_s

    partial_string_size = n % len(s)
    for position in range(0, partial_string_size):
        if s[position] == 'a':
            number_of_a += 1

    return number_of_a


s = 'aba'
n = 10
print('Should be 7, was: ', end='')
print(repeatedString(s, n))

s = 'a'
n = 1000000000000
print('Should be 1000000000000, was: ', end='')
print(repeatedString(s, n))

s = 'abcac'
n = 10
print('Should be 4, was: ', end='')
print(repeatedString(s, n))
