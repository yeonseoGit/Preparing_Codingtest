import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())     # 컴퓨터 수
m = int(input())     # 연결 수

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

visited = [False] * n

def dfs(v):
    visited[v] = True
    for next in graph[v]:
        if not visited[next]:
            dfs(next)

dfs(0)
print(visited.count(True) - 1)
