from collections import namedtuple

n = int(input())
fields = input().split()
Student = namedtuple('Student', fields)
marks = [int(Student._make(input().split()).MARKS) for _ in range(n)]
print('{:.2f}'.format(sum(marks)/n))
