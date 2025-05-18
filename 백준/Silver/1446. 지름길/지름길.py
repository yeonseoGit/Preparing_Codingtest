import sys

input = sys.stdin.readline

n, d = map(int, input().split())
shortcuts = []

for _ in range(n):
    start, end, cost = map(int, input().split())
    if end <= d:  # 도착 지점을 넘는 지름길은 무시
        shortcuts.append((start, end, cost))

# dp[i]: 0부터 i까지 가는 최소 거리
dp = [i for i in range(d + 1)]  # 일단은 전부 일반도로로 간다고 초기화

# 0부터 d까지 차례대로 확인
for i in range(d + 1):
    if i != 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)  # 일반 도로로 1만큼 가는 경우

    for start, end, cost in shortcuts:
        if start == i:
            if dp[end] > dp[start] + cost:
                dp[end] = dp[start] + cost

print(dp[d])
