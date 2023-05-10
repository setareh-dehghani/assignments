from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)

combs = combinations_with_replacement(sorted(s), k)

for c in combs:
    print("".join(c))
