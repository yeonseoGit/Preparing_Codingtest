import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
f_1, f_2 = map(int, input().split())
m = int(input())

family = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

answer = 0
visit = [-1] * (n + 1)

def bfs(x, y):
    q = deque()
    q.append(x)
    visit[x] = 0

    while q:
        c_x = q.popleft()
        for i in family[c_x]:
            if visit[i] == -1:
                visit[i] = visit[c_x] + 1
                q.append(i)
    return visit[y]

print(bfs(f_1, f_2))
