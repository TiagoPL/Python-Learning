import os


# Complete the rotLeft function below.
def rotLeft(a, d):
    list_copy = []
    list_copy.append(a[n - 1])

    for rotations in range(0, d):
        list_copy.append(a[rotations])
    for rest in range(n - 2, d - 1, -1):
        list_copy.insert(0, a[rest])

    return list_copy


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
