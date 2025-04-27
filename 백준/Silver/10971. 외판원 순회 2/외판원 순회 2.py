import sys
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
ans = int(1e9)

def dfs(start, now, cost, depth):
    global ans
    if depth == n:
        if w[now][start] != 0:
            ans = min(ans, cost + w[now][start])
        return
    for next in range(n):
        if not visited[next] and w[now][next] != 0:
            visited[next] = True
            dfs(start, next, cost + w[now][next], depth + 1)
            visited[next] = False

for i in range(n):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(ans)
