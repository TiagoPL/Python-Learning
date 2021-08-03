import timeit

fact_test = '''\
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result

x = fact(130)
'''

factorial_test = '''\
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

y = factorial(130)
'''

result_1 = timeit.timeit(fact_test, number=1000)
result_2 = timeit.timeit(factorial_test, number=1000)

print()
print(f'Result 01:          {result_1:.5f}')
print(f'Result 02:          {result_2:.5f}')
