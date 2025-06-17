import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

games_cir = [int(input()) for _ in range(n)]
cnt = 0
visit = [False]*(n)
q = deque()
q.append(0)
while q :
    cur = q.popleft()
    if visit[cur] :
        cnt = -1
        break
    if cur == k :
        break

    visit[cur] = True
    q.append(games_cir[cur])
    cnt += 1
print(cnt)
