import sys
from itertools import combinations
import copy # 깊은 복사를 위함! 

input = sys.stdin.readline

n, m = map(int, input().split())
jido =  [list(map(int, input().split())) for _ in range(n)] # n&m 

wall = []
for i in range(n) : # 벽을 세우기 위한 벽위치 리스트 만들기
    for j in range(m):
        if jido[i][j] == 0 : # 빈공간인 곳만 벽 세울 수 있기 때문에 조건 추가.
            wall.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visit = [[False]*m for _ in range(n)]

def dfs(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if jido_w[nx][ny] == 0:
                jido_w[nx][ny] = 2
                dfs(nx, ny)
add_wall = list(combinations(wall, 3))

max_safe = 0
for i in range(len(add_wall)) :
    jido_w = copy.deepcopy(jido) # 원본 살려두기.
    for j in [0, 1, 2] :    
        x, y = add_wall[i][j]
        jido_w[x][y] = 1
    for i in range(n):
        for j in range(m):
            if jido_w[i][j] == 2:
                dfs(i, j)
    count = 0
    for i in range(n):
        for j in range(m):
            if jido_w[i][j] == 0:
                count += 1
    max_safe = max(max_safe, count)
    # bfs 든 dfs 든 여기서 함수실행! 
    # 내가 봤을 때, dfs가 더 쉬울둣! 왜냐면 큐를 쓰는 것보다 그냥 깊이로 쭉 다 검사하는게 나아보임.  


print(max_safe)