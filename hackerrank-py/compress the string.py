from itertools import groupby

# read the input string
s = input().strip()

# use groupby to group consecutive characters and count their occurrences
compressed = [(len(list(group)), int(char)) for char, group in groupby(s)]

# print the compressed string
print(' '.join(f"({count}, {char})" for count, char in compressed))
