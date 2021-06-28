def sockMerchant(n, ar):
    answer = 0
    ar_set = set(ar)

    for number in ar_set:
        answer += ar.count(number) // 2

    return answer


n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
result = sockMerchant(n, ar)
print(result)
