def commonChild(s1, s2):
    current_count = 0
    temporary_count = 0
    highest_count = 0
    last_letter_position = -1

    for position, letter in enumerate(s2):
        for position2, other_letter in enumerate(s1):
            if letter == other_letter and position > last_letter_position:
                current_count += 1
                last_letter_position = position
        if current_count > temporary_count:

            temporary_count = current_count
            current_count = 0

        if temporary_count > highest_count:
            highest_count = temporary_count

    return highest_count






s1 = 'HARRY'
s2 = 'SALLY'
result = commonChild(s1, s2)
print(f'Should be 2, was {result}')
print('=' * 30)

s1 = 'AA'
s2 = 'BB'
result = commonChild(s1, s2)
print(f'Should be 0, was {result}')
print('=' * 30)

s1 = 'SHINCHAN'
s2 = 'NOHARAAA'
result = commonChild(s1, s2)
print(f'Should be 3, was {result}')
print('=' * 30)

s1 = 'ABCDEF'
s2 = 'FBDAMN'
result = commonChild(s1, s2)
print(f'Should be 2, was {result}')
print('=' * 30)
