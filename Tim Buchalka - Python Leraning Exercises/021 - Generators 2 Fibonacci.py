def fibonacci():
    current = 0
    previous = 1
    while True:
        yield current
        current, previous = current + previous, current


fib = fibonacci()

for n in range(0, 21):
    print(f'f{n} - ', next(fib))
