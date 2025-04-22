import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
dp = list(map(int, input().split()))

# DP 배열: N+1 x M+1 크기 (곡 개수 + 볼륨 크기)
volume = [[False]*(M+1) for _ in range(N+1)]
volume[0][S] = True  # 시작 볼륨 설정

for i in range(N):
    for v in range(M+1):
        if volume[i][v]:
            if v + dp[i] <= M:
                volume[i+1][v + dp[i]] = True
            if v - dp[i] >= 0:
                volume[i+1][v - dp[i]] = True

for i in range(M, -1, -1):
    if volume[N][i]:
        print(i)
        break
else:
    print(-1)
