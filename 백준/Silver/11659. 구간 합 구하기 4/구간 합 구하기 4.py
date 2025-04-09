import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
pre = [0]
curr = 0
for i in range(N):
    curr += nums[i]
    pre.append(curr)

for _ in range(M) :
    i, j = map(int, input().split())
    print(pre[j] - pre[i-1])