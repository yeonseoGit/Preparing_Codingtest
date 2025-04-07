import sys
Input = sys.stdin.readline

def dfs(node, cnt):
    visited[node] = 1
    
    for adj_node in graph[node]:
        if visited[adj_node] == 0:
            cnt = dfs(adj_node, cnt+1)
    
    return cnt

T = int(Input())
for _ in range(T):
    N, M = map(int, Input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    
    for _ in range(M):
        a, b = map(int, Input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    print(dfs(1, 0))