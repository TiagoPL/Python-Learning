import os


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    answer = 0
    ar_set = set(ar)

    for number in ar_set:
        answer += ar.count(number) // 2

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
