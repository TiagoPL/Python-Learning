# for x in range(1, 31):
#     fizzbuzz = 'Fizz buzz' if x % 15 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else str(x)
#     print(fizzbuzz)
#
fizzbuzz = ['fizzbuzz' if x % 15 == 00 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else str(x) for x in range(1, 31)]
print(fizzbuzz)
