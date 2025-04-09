import sys

input = sys.stdin.readline
n = int(input())

dp = [1, 2]
if n > 2 :
    for i in range(2, n):
        dp.append(dp[i-2] + dp[i-1])
    print(dp[-1]% 10007)
else :
    print(dp[n-1])