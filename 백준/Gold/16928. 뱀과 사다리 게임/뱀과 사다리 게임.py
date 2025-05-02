import sys
from collections import deque

input = sys.stdin.readline

# 주사위를 조작해 내가 원하는 수가 나오게 만들 수 있다면, 최소 몇 번만에 도착점에 도착
# 입력 처리
n, m = map(int, input().split())
board = [i for i in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    board[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    board[u] = v

visited = [False] * 101
q = deque()
q.append((1, 0))
visited[1] = True

while q:
    pos, cnt = q.popleft()
    if pos == 100:
        print(cnt)
        break
    for dice in range(1, 7):  # 주사위 1~6
        next_pos = pos + dice
        if next_pos <= 100 and not visited[board[next_pos]]:
            visited[board[next_pos]] = True
            q.append((board[next_pos], cnt + 1))
