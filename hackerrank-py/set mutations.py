n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    command, num = input().split()
    other_set = set(map(int, input().split()))

    if command == 'update':
        s |= other_set
    elif command == 'intersection_update':
        s &= other_set
    elif command == 'difference_update':
        s -= other_set
    elif command == 'symmetric_difference_update':
        s ^= other_set

print(sum(s))
