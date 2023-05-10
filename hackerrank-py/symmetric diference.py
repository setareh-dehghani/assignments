# Read the input values
M = int(input())
set_a = set(map(int, input().split()))
N = int(input())
set_b = set(map(int, input().split()))

# Compute symmetric difference
symmetric_diff = set_a.symmetric_difference(set_b)

# Print the result in ascending order
for num in sorted(symmetric_diff):
    print(num)
