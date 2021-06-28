import math


def primality(n):
    answer = ''

    if n == 1:
        answer = 'Not prime'
        return answer

    if n == 2 or n == 3:
        answer = 'Prime'
        return answer

    if n >= 4:
        answer = 'Prime'

        for number in range(2, math.floor(math.sqrt(n)) + 1):
            if n % number == 0:
                answer = 'Not prime'
                break

    return answer


n = 1
result = primality(n)
print(result)

n = 4
result = primality(n)
print(result)

n = 9
result = primality(n)
print(result)

n = 907
result = primality(n)
print(result)
