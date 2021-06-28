def minimumBribes(q):

    moves = 0

    q = [person - 1 for person in q]

    for index, person in enumerate(q):

        if person - index > 2:
            print("Too chaotic")
            break

        for j in range(max(person - 1, 0), index):
            if q[j] > person:
                moves += 1

    print(moves)
