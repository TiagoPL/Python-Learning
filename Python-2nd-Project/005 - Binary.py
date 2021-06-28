with open('Binary', 'bw') as bin_file:
    for number in range(0, 17):
        bin_file.write(bytes([number]))

with open('Binary', 'br') as binFile:
    for b in binFile:
        print(b)

# =====================================================

with open('Binary', 'bw') as bin_file:
    bin_file.write(bytes(range(0, 17)))

with open('Binary', 'br') as binFile:
    for b in binFile:
        print(b)

# =====================================================

with open('Binary', 'br') as bin_file:              # Retornando valor errado
    e = int.from_bytes(bin_file.read(), 'little')
    print(e)
