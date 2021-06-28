#!/bin/python3


def countingValleys(steps, path):
    valley_count = 0
    position = 0
    for step in path:
        if step == "U":
            position += 1
        else:
            if position == 0:
                valley_count += 1
            position -= 1
    return valley_count


result = countingValleys(8, "UDDDUDUU")
print(result)
