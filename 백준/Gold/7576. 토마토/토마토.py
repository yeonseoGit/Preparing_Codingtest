import sys
from collections import deque

Input = sys.stdin.readline
M, N = map(int, Input().split())

box = []
for i in range(N):
    box.append(list(map(int, Input().split())))

queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1 :
            queue.append([i,j])

def bfs():
    while queue:
        x, y = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

bfs()

day = 0
for row in box:
    for i in row:
        if i == 0:  
            print(-1)
            exit()
    else: 
        day = max(day, max(row))

print(day-1)