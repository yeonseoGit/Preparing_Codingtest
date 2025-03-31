import sys
input = sys.stdin.readline

N = int(input())
ans = [int(input()) for _ in range(N)]

ans.sort()

for num in ans:
    print(num)
