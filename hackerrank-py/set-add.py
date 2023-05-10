n = int(input())
stamps = set()

for _ in range(n):
    stamp = input().strip()
    stamps.add(stamp)

print(len(stamps))
