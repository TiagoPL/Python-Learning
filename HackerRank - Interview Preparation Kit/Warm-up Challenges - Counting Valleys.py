def countingValleys(steps, path):
    answer = 0
    position = 0
    for letter in path:
        if letter == 'U':
            position += 1
        elif letter == "D" and position == 0:
            position -= 1
            answer += 1
        else:
            position -= 1

    return answer


steps = 8
path = 'UDDDUDUU'
result = countingValleys(steps, path)
print(result)
