import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

m, n, k = map(int, input().split())
visited = [[0]*n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            visited[i][j] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    visited[x][y] = 1
    area = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0:
            area += dfs(nx, ny)
    return area

result = []
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            result.append(dfs(i, j))

result.sort()
print(len(result))
print(' '.join(map(str, result)))
