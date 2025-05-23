import sys
from collections import deque

input = sys.stdin.readline

x, y = map(int, input().split())
jido = [list(input().strip()) for _ in range(x)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(mx, my):
    visit = [[-1]*y for _ in range(x)]
    q = deque()
    q.append([mx, my])
    visit[mx][my] = 0
    max_dist = 0
    while q :
        cmx, cmy = q.popleft()
        for i in range(4):
            fx = cmx+dx[i]
            fy = cmy+dy[i]
            if 0 <= fx < x and 0 <= fy < y :
                if jido[fx][fy] == 'L' and visit[fx][fy] == -1 :
                    visit[fx][fy] = visit[cmx][cmy] + 1
                    max_dist = max(max_dist, visit[fx][fy])
                    q.append([fx, fy])
    return max_dist

answer = 0
for i in range(x):
    for j in range(y):
        if jido[i][j] == 'L':
            answer = max(answer, bfs(i, j))
print(answer)