from collections import deque

d = deque()
n = int(input())

for i in range(n):
    operation = input().split()

    if operation[0] == "append":
        d.append(int(operation[1]))
    elif operation[0] == "appendleft":
        d.appendleft(int(operation[1]))
    elif operation[0] == "pop":
        d.pop()
    elif operation[0] == "popleft":
        d.popleft()

print(*d)
