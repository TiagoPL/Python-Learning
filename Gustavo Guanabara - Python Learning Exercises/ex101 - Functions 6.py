from datetime import date


def vote(n):
    if date.today().year - n < 16:
        return'Vote DENIED'
    elif (date.today().year - n > 15) and (date.today().year - n < 18):
        return 'Vote OPTIONAL'
    elif date.today().year - n > 64:
        return'Vote OPTIONAL'
    else:
        return'Vote MANDATORY'


n1 = int(input('Enter your year of birth: '))
print(f'With {date.today().year - n1} years: {vote(n1)}.')
