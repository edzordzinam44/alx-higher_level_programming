#!/usr/bin/python3
for j in range(ord('a'), ord('z') + 1):
    # Check if the character is not 'q' and not 'e'
    if chr(j) != 'q' and chr(j) != 'e':
        print('{:c}'.format(j), end='')
