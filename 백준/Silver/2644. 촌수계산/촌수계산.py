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

visit = [-1] * (n + 1)

def dfs(x, count):
    visit[x] = count
    for i in family[x]:
        if visit[i] == -1:
            dfs(i, count + 1)

dfs(f_1, 0)
print(visit[f_2])