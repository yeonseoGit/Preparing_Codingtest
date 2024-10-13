import sys

n = int(input())
c = []
d = [[]]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    c.append(a+b)
    d.append([a, b])

for j in range(n):
    print(f'Case #{j+1}: {d[j+1][0]} + {d[j+1][1]} = {c[j]}')