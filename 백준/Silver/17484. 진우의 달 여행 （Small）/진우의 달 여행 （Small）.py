import sys
input = sys.stdin.readline

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]

dp = [[[float('inf')]*3 for _ in range(M)] for _ in range(N)] # "이전에 어디서 왔는지" 상태를 기억해야 함. 
# 최솟값을 찾는 DP니까, 초기값을 매우 큰 값으로 설정 -> min()을 쓸 때 방해되지 않게

# 초기 설정
for j in range(M):
    for d in range(3) : # 0 : 왼쪽, 1 : 가운데, 2 : 오른쪽
        dp[0][j][d] = space[0][j] # 어차피 처음에 왼쪽 오른쪽 가운데 이런게 없음

# 초기 설정 제외 진짜 돌아가는 점화식 부분
for i in range(1, N): # N번째 줄
    for j in range(M): # M번째 값
        for d in range(3):
            pre = j + [-1,0,1][d] # 현재 위치 j에 도달하기 위해 직전에 어떤 열에서 왔는지를 계산
            # [2, 3, 0, -1][3] 이렇게 되면 0임. 즉, 리스트의 인덱스 접근이야. 
            if 0 <= pre <M :
                for pred in range(3):
                    if pred != d:
                        dp[i][j][d] = min(dp[i][j][d], dp[i-1][pre][pred]+ space[i][j])

result = 1000000
for j in range(M):
    for d in range(3):
        result = min(result , dp[N-1][j][d])

print(result)