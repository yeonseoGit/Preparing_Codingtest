import sys
from collections import deque

n, m = map(int, input().split())

picture = [list(map(int, input().split())) for _ in range(n)]

queue = deque()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue.append((x, y))
    picture[x][y] = 0  # 방문 처리
    area = 1
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m) :
                if picture[nx][ny] == 1 :
                    queue.append((nx, ny))
                    picture[nx][ny] = 0
                    area += 1

    return area

count = 0
max_area = 0 

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1:
            count += 1
            max_area = max(max_area, bfs(i, j))

print(count)
print(max_area)