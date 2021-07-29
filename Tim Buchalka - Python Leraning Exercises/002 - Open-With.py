text = open('/Sample.txt', 'r')
for line in text:
    print(line, end='')
text.close()

# ===========================================================================

with open('/Sample.txt', 'r') as text:
    for line in text:
        print(line, end='')

# ===========================================================================

with open('/Sample.txt', 'r') as text:
    all_lines = text.readlines()
for line in all_lines:
    print(line, end='')
