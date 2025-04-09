import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [1, 1, 1, 2, 2]
    if N > 5 :
        for i in range(5, N):
            dp.append(dp[i-3]+dp[i-2])
    print(dp[N-1])