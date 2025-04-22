import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

R, C = map(int, input().split())

maps = []
while len(maps) < R:
    line = input().strip()
    if line:
        maps.append(list(line))

visited = [[0]*C for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    visited[x][y] = 1
    if maps[x][y] == 'o':
        cnt[0] += 1
    elif maps[x][y] == 'v':
        cnt[1] += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0:
            if maps[nx][ny] != '#':
                dfs(nx, ny)

total_sheep = 0
total_wolf = 0

for i in range(R):
    for j in range(C):
        if visited[i][j] == 0 and maps[i][j] != '#':
            cnt = [0, 0]
            dfs(i, j)
            if cnt[0] > cnt[1]:
                total_sheep += cnt[0]
            else:
                total_wolf += cnt[1]

print(total_sheep, total_wolf)
