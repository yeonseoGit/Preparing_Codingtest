# 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정
import sys
from collections import deque
#bfs
input = sys.stdin.readline
n = int(input())
local = [list(map(int, input().split())) for _ in range(n)]

# 좌우상하
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# local 내 최대 높이 찾기
max_height = max(map(max, local))
answer = 0

def bfs(x, y, h, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True # 2차원 배열이니깐!

    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and local[nx][ny] > h:
                    visited[nx][ny] = True
                    q.append((nx, ny))

for h in range(0, max_height + 1):  # 비가 하나도 안올 때부터 최대 높이까지
    visited = [[False]*n for _ in range(n)]
    cnt = 0  # 안전 영역 수

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and local[i][j] > h:
                bfs(i, j, h, visited)
                cnt += 1
    answer = max(answer, cnt)

print(answer)