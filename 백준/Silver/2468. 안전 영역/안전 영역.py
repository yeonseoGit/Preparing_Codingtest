# dfs로 풀었을 때!
import sys
sys.setrecursionlimit(10000)  # ← 충분히 넉넉하게
input = sys.stdin.readline

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, h, visit):
    visit[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < n :
            if visit[nx][ny] == False and space[nx][ny] > h:
                dfs(nx, ny, h, visit)

m_h = max(map(max, space))
ans = 0

for h in range(0, m_h):
    visit = [[False]*n for _ in range(n)]
    cnt = 0 

    for i in range(0, n):
        for j in range(0, n):
            if visit[i][j] == False and space[i][j] > h:
                dfs(i, j, h, visit)
                cnt += 1
    ans = max(ans, cnt)

print(ans)