N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 2)

# 역순으로 DP 계산
for i in range(N, 0, -1):
    time, profit = schedule[i-1]
    if i + time <= N + 1:
        dp[i] = max(dp[i+1], profit + dp[i + time])
    else:
        dp[i] = dp[i+1]

print(dp[1])

'''N = int(input())
best_day = []
for i in range(0, N):
    best_day.append(list(map(int, input().split())))
day = 1
money = 0
while day < N :
    day += best_day[day-1][0]
    money += best_day[day-1][1]
        
print(money)

N = int(input())
best_day = []
for i in range(0, N):
    best_day.append(list(map(int, input().split())))

day = 1
money = 0

while day <= N:
    next_day, earn = best_day[day-1]
    money += earn
    day += next_day
    if day > N:  # day가 N을 초과하면 종료
        break

print(money)
'''