N = int(input())

graph = []

for i in range(N) :
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
    
    if graph[x][y] == 1:
        graph[x][y] = 0 
        count = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            count += dfs(nx, ny)
        return count
    return 0

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(dfs(i, j))

print(len(result))
for r in sorted(result):
    print(r)
