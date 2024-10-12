import sys

N = int(input())
c = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    c.append(a+b)

for j in range(N):
    print(f'Case #{j+1}: {c[j]}')