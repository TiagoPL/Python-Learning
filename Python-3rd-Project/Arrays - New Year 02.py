def minimumBribes(q):
    chaotic = False
    steps = 0

    for number in q:
        if number > q.index(number) + 3:
            chaotic = True
            break

    for number in range(n - 1, -1, -1):
        for test in range(q.index(q[number]) - 1, -1, -1):
            if q[test] > q[number]:
                steps += 1

    if chaotic:
        print('Too chaotic')
    else:
        print(steps)


n = 8
q = [1, 2, 5, 3, 7, 8, 6, 4]
minimumBribes(q)
