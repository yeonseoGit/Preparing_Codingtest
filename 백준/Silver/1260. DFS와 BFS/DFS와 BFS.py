from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for neighbor in sorted(graph[v]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, v):
    visited = [False] * (len(graph) + 1)
    queue = deque([v])
    visited[v] = True

    while queue:
        current = queue.popleft()
        print(current, end=' ')

        for neighbor in sorted(graph[current]):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 실행
visited = [False] * (n + 1)
dfs(graph, v, visited)
print()
# BFS 실행
bfs(graph, v)

