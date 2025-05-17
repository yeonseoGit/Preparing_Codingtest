import sys

input = sys.stdin.readline
n = int(input())

tri = [list(map(int, input().split())) for _ in range(n)]


# DP를 triangle 배열을 재활용하여 사용
for i in range(1, n):
    for j in range(i+1):
        # 왼쪽 끝 값 (오른쪽 위에서만 올 수 있음)
        if j == 0:
            tri[i][j] += tri[i-1][j]
        # 오른쪽 끝 값 (왼쪽 위에서만 올 수 있음)
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
        # 가운데 값 (양쪽 위에서 모두 올 수 있음)
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

# 맨 마지막 줄 중 최대값 출력
print(max(tri[-1]))