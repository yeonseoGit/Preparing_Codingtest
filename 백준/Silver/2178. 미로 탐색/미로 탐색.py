import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if miro[nx][ny] == 1 :
                    miro[nx][ny] = miro[x][y] + 1
                    queue.append((nx, ny))
    return miro[N-1][M-1]

print(bfs(0, 0))
