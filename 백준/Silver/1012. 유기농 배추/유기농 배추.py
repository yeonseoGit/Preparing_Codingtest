import sys
sys.setrecursionlimit(10**9)

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N or graph[y][x] == 0:
        return False
    graph[y][x] = 0
    for l in range(4):
        nx = x + dx[l]
        ny = y + dy[l]
        dfs(nx, ny)
    return True

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1
    result = 0 
    for i in range(N):
        for j in range(M):
            if dfs(j, i):
                result += 1
    print(result)
