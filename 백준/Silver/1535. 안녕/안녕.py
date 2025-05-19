import sys

input = sys.stdin.readline

n = int(input())

less = list(map(int, input().split()))
joy = list(map(int, input().split()))

dp = [0] * 101

for i in range(n):
    for hp in range(100, less[i] - 1, -1):
        dp[hp] = max(dp[hp], dp[hp - less[i]] + joy[i])

print(max(dp[:100]))