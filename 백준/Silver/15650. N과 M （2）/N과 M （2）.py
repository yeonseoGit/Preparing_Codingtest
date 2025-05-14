n, m = map(int, input().split())
visited = [False] * (n + 1)
result = []

def dfs(start, depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, n + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(i + 1, depth + 1)
            result.pop()
            visited[i] = False

dfs(1, 0)
