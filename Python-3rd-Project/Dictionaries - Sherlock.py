from collections import Counter


def sherlockAndAnagrams(s):
    all_sub_strings_list = [[s[j:j + i] for j in range(len(s) - i + 1)] for i in range(1, len(s))]

    counter_dictionary = Counter()
    answer = 0

    for sub_string_list in all_sub_strings_list:
        for sub_string in sub_string_list:
            clean_sub_string = ''.join(sorted(sub_string))
            counter_dictionary[clean_sub_string] += 1

    for sub_string in counter_dictionary:
        answer += int(counter_dictionary[sub_string] * (counter_dictionary[sub_string] - 1) / 2)

    return answer


s = 'abba'
result = sherlockAndAnagrams(s)
print(f'Should be "4",  was "{result}".')

s = 'acbd'
result = sherlockAndAnagrams(s)
print(f'Should be "0",  was "{result}".')

s = 'ifailuhkqq'
result = sherlockAndAnagrams(s)
print(f'Should be "3",  was "{result}".')

s = 'kkkk'
result = sherlockAndAnagrams(s)
print(f'Should be "10", was "{result}".')

s = 'cdcd'
result = sherlockAndAnagrams(s)
print(f'Should be "5",  was "{result}".')
