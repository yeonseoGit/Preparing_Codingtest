import sys

input = sys.stdin.readline

N = int(input())
jido = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
dx = [0, 1]  # 오른쪽, 아래쪽
dy = [1, 0]

def dfs(x, y):
    if jido[x][y] == -1:
        return True

    move = jido[x][y]
    for i in range(2):
        nx = x + dx[i] * move
        ny = y + dy[i] * move

        if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            if dfs(nx, ny):
                return True
    return False

visit[0][0] = 1
if dfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")
