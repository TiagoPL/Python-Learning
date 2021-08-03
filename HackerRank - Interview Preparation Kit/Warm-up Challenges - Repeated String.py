import os


# Complete the repeatedString function below.
def repeatedString(s, n):
    a_in_string = 0
    total_a = 0
    for letter in s:
        if letter == 'a':
            a_in_string += 1

    clean_ones = n // len(s)
    clean_add = clean_ones * a_in_string
    total_a += clean_add

    letters_left = n % len(s)
    for letter in range(0, letters_left):
        if s[letter] == 'a':
            total_a += 1

    return total_a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
