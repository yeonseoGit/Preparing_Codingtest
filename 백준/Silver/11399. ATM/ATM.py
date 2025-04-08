import sys
Input = sys.stdin.readline

N = int(Input())
peoples = list(map(int, Input().split()))
peoples.sort()

dp = [0]*N
sum = 0
for i in range(N):
    if i == 0 :
        dp[i] = peoples[i]
        sum += dp[i]
    else :
        dp[i] = dp[i-1]+peoples[i]
        sum += dp[i]
print(sum)