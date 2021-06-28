from collections import Counter


def arrayManipulation(n, queries):
    c = Counter()

    for a, b, k in queries:
        c[a] += k
        c[b+1] -= k

    array_sum = 0
    max_sum = 0
    for item in sorted(c)[:-1]:
        array_sum += c[item]
        max_sum = max(max_sum, array_sum)

    return max_sum


n = 5
queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
result = arrayManipulation(n, queries)
print()
print(f'The result was {result}')
print('=' * 40)
