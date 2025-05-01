import sys
from collections import deque

q = deque()

input = sys.stdin.readline

m, n, h = map(int, input().split())

apple_box = []
for _ in range(h):
    apples = [list(map(int, input().split())) for _ in range(n)]
    apple_box.append(apples)

visited = [[[False]*m for _ in range(n)] for _ in range(h)]
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if apple_box[i][j][k] == 1 :
                visited[i][j][k] = True
            elif apple_box[i][j][k] == -1 :
                visited[i][j][k] = -1

q = deque()

# 익은 토마토 시작점만 큐에 넣음
for z in range(h):
    for y in range(n):
        for x in range(m):
            if apple_box[z][y][x] == 1:
                q.append((z, y, x))

day = -1  # 처음엔 -1, 첫 루프에서 0일차가 됨

while q:
    for _ in range(len(q)):  # 현재 큐 길이만큼만 처리 (하루치)
        z, y, x = q.popleft()
        for d in range(6):
            nz = z + dz[d]
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if apple_box[nz][ny][nx] == 0:
                    apple_box[nz][ny][nx] = 1
                    q.append((nz, ny, nx))
    day += 1

for layer in apple_box:
    for row in layer:
        if 0 in row:
            print(-1)
            exit()

print(day)
