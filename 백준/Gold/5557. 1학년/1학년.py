# 2차원 DP (or 딕셔너리 배열) 
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [[0]*21 for _ in range(N)]

dp[0][nums[0]] = 1

for i in range(N-1):
    for s in range(21):
        if dp[i][s] > 0 : 
            if s + nums[i+1] <= 20 : 
                dp[i+1][s+nums[i+1]] += dp[i][s]
            if s - nums[i+1] >= 0 :
                dp[i+1][s-nums[i+1]] += dp[i][s]

print(dp[N-2][nums[N-1]])
