import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())

q_j = deque()
q_f = deque()
miro = [list(input().strip()) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
fire_time = [[-1]*n for _ in range(m)]
jihun_time = [[-1]*n for _ in range(m)]

for y in range(m):
    for x in range(n):
        if miro[y][x] == 'J':
            q_j.append((y, x))
            jihun_time[y][x] = 0  # ✅ 시작 지점 시간 0으로 설정
        elif miro[y][x] == 'F':
            q_f.append((y, x))
            fire_time[y][x] = 0  # ✅ 불도 시간 0부터 시작해야 퍼질 수 있음

while q_f:
    y, x = q_f.popleft()
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < m and 0 <= nx < n:
            if miro[ny][nx] != '#' and fire_time[ny][nx] == -1:
                fire_time[ny][nx] = fire_time[y][x] + 1
                q_f.append((ny, nx))

while q_j:
    y, x = q_j.popleft()
    if y == 0 or y == m-1 or x == 0 or x == n-1:
        print(jihun_time[y][x] + 1)
        exit()
    
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < m and 0 <= nx < n:
            if miro[ny][nx] != '#' and jihun_time[ny][nx] == -1:
                if fire_time[ny][nx] == -1 or fire_time[ny][nx] > jihun_time[y][x] + 1: #불이 더 늦게 번진다는 뜻
                    jihun_time[ny][nx] = jihun_time[y][x] + 1
                    q_j.append((ny, nx))

print("IMPOSSIBLE")
