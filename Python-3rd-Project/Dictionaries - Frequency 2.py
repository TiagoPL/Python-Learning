from collections import defaultdict


def freqQuery(queries):
    answer = []
    structure = defaultdict(int)
    for array in queries:
        if array[0] == 1:
            structure[array[1]] += 1
        elif array[0] == 2:
            if array[1] in structure and structure[array[1]] > 0:
                structure[array[1]] -= 1
        else:
            answer.append(1 if array[1] in set(structure.values()) else 0)
    return answer


queries = [(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]
ans = freqQuery(queries)
print(ans)
print(f'[0, 1] - Correct')
print('=' * 20)

queries = [(1, 5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5), (3, 2)]
ans = freqQuery(queries)
print(ans)
print(f'[0, 1] - Correct')
print('=' * 20)

queries = [(3, 4), (2, 1003), (1, 16), (3, 1)]
ans = freqQuery(queries)
print(ans)
print(f'[0, 1] - Correct')
print('=' * 20)

queries = [(1, 3), (2, 3), (3, 2), (1, 4), (1, 5), (1, 5), (1, 4), (3, 2), (2, 4), (3, 2)]
ans = freqQuery(queries)
print(ans)
print(f'[0, 1, 1] - Correct')
print('=' * 20)

queries = [(1, 3), (1, 38), (2, 1), (1, 16), (2, 1), (2, 2), (1, 64), (1, 84), (3, 1), (1, 100),
           (1, 10), (2, 2), (2, 1), (1, 67), (2, 2), (3, 1), (1, 99), (1, 32), (1, 58), (3, 2)]
ans = freqQuery(queries)
print(ans)
print(f'[1, 1, 0] - Correct')
print('=' * 20)
