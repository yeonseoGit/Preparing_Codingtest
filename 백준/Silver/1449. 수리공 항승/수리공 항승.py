import sys
input = sys.stdin.readline

n, l = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()

count = 1 
start = leak[0]

for i in range(1, n):
    if leak[i] - start + 0.5 > l:
        count += 1
        start = leak[i]

print(count)