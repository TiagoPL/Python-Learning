import collections


def isValid(s):
    s = s.replace('\n', '')
    s_set = set(s)
    results = []
    answer = ''
    chance = 1

    for letter in s_set:
        results.append(s.count(letter))
    results = sorted(results)

    default_value = collections.Counter(results).most_common(1)[0][0]

    for number in sorted(results):
        try:
            if default_value != number:
                if chance == 0:
                    answer = 'NO'
                    break
                else:
                    chance -= 1
        except IndexError:
            pass

    if answer == '':
        for number in results:
            chance = 1
            for other_number in results:
                if other_number < number - 1:
                    if default_value != number:
                        if chance == 0:
                            answer = 'NO'
                            # print('Stopped Here 1')
                            break
                        else:
                            chance -= 1
                elif other_number > number + 1:
                    if default_value != number:
                        if chance == 0:
                            answer = 'NO'
                            # print('Stopped Here 2')
                            break
                        else:
                            chance -= 1
                else:
                    answer = 'YES'

    # print(results)
    return answer


s = 'abc'
result = isValid(s)
print(f'Expected: YES, Got: {result}')
print('=' * 30)

s = 'abcc'
result = isValid(s)
print(f'Expected: YES, Got: {result}')
print('=' * 30)

s = 'aabbc'
result = isValid(s)
print(f'Expected: YES, Got: {result}')
print('=' * 30)

s = 'abccc'
result = isValid(s)
print(f'Expected: NO,  Got: {result}')
print('=' * 30)

s = 'aabbcd'
result = isValid(s)
print(f'Expected: NO,  Got: {result}')
print('=' * 30)

s = '''ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchd
fabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhh
ehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbche
bheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgdd
bbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehb
bfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgb
dcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecga
iiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebge
hiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'''
result = isValid(s)
print(f'Expected: YES, Got: {result}')
print('=' * 30)
