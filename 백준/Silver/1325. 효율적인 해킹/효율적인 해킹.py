import sys
from collections import deque

input = sys.stdin.readline

n, m  = map(int, input().split())

computer = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # b를 해킹하면 a도 가능 → 역방향 저장
    computer[b].append(a)

# 먼저 queue를 활용한 bfs
def bfs(x) :
    visit = [False]*(n+1)
    visit[x] = True
    q = deque()
    q.append(x)
    count = 1

    while q :
        now = q.popleft()
        for i in computer[now] :
            if visit[i] == False :
                visit[i] = True
                q.append(i)
                count += 1
    return count

result = []
max_count = 0

for i in range(1, n + 1):
    c = bfs(i)
    if c > max_count:
        max_count = c
        result = [i]
    elif c == max_count:
        result.append(i)

print(*result)