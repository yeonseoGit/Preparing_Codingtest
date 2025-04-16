from collections import deque

n, m = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(n)]
result = [[-1]*m for _ in range(n)]

# 시작 지점
for i in range(n):
    for j in range(m):
        if jido[i][j] == 2:
            start_x, start_y = i, j
        elif jido[i][j] == 0:
            result[i][j] = 0 

queue = deque()
queue.append((start_x, start_y))
result[start_x][start_y] = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if jido[nx][ny] == 1 and result[nx][ny] == -1:
                result[nx][ny] = result[x][y] + 1
                queue.append((nx, ny))


for row in result:
    print(*row)
