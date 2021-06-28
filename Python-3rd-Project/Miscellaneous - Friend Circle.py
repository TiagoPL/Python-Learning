def maxCircle(queries):

    for list in queries:
        print(len(queries[0]))

        


queries = [[1, 2], [1, 3]]
ans = maxCircle(queries)
print(f'''Expected Output:
2
3''')
print('=' * 20)

queries = [[1000000000, 23], [11, 3778], [7, 47], [11, 1000000000]]
ans = maxCircle(queries)
print(f'''Expected Output:
2
2
2
4''')
print('=' * 20)

queries = [[1, 2], [3, 4], [1, 3], [5, 7], [5, 6], [7, 4]]
ans = maxCircle(queries)
print(f'''Expected Output:
2
2
4
4
4
7''')
print('=' * 20)
