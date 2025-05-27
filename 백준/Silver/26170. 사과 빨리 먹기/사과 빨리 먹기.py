import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

bord = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

apple = 0
result = float('inf')
visit = [[False] * 5 for _ in range(5)]

def dfs(x, y, dist):
    global apple, result

    if apple == 3:
        result = min(result, dist)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if not visit[nx][ny] and bord[nx][ny] != -1:
                visit[nx][ny] = True
                is_apple = False
                if bord[nx][ny] == 1:
                    apple += 1
                    is_apple = True

                dfs(nx, ny, dist + 1)

                if is_apple:
                    apple -= 1
                visit[nx][ny] = False

# 시작 위치에 사과가 있을 경우 먼저 처리
if bord[r][c] == 1:
    apple = 1
    bord[r][c] = 0  # 먹은 걸로 처리
visit[r][c] = True
dfs(r, c, 0)

print(result if result != float('inf') else -1)