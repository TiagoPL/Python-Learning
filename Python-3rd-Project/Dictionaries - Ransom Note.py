from collections import Counter


def checkMagazine(magazine, note):
    a = Counter(magazine)
    b = Counter(note)

    for word, number in b.items():
        if word not in a:
            print('No')
            return
        elif number > a[word]:
            print('No')
            return
    print('Yes')




    # if (a & b) == b:
    #     print('Yes')
    # else:
    #     print("No")


magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
note = ['give', 'one', 'grand', 'today']
print(f'Should be "Yes", was: ', end='')
checkMagazine(magazine, note)

magazine = ['two', 'times', 'three', 'is', 'not', 'four']
note = ['two', 'times', 'two', 'is', 'four']
print(f'Should be "No",  was: ', end='')
checkMagazine(magazine, note)

magazine = ['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts']
note = ['ive', 'got', 'some', 'coconuts']
print(f'Should be "No",  was: ', end='')
checkMagazine(magazine, note)
