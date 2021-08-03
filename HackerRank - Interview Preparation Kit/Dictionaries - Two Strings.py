import os


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1 = set(s1)
    s2 = set(s2)

    for letter in s1:
        for other_letter in s2:
            if other_letter == letter:
                return 'YES'

    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
