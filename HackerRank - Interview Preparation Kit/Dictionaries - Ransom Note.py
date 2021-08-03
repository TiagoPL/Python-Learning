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


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
