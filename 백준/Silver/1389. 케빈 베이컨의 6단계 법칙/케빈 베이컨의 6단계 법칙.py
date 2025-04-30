import sys
input = sys.stdin.readline

N, M = map(int, input().split())

friends = [list(map(int, input().split())) for _ in range(M)]

INF = int(1e9)
dist = [[INF] * N for _ in range(N)]

for i in range(N):
    dist[i][i] = 0

for a, b in friends:
    dist[a-1][b-1] = 1
    dist[b-1][a-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
min_sum = INF
answer = 0
for i in range(N):
    total = sum(dist[i])
    if total < min_sum:
        min_sum = total
        answer = i

print(answer+1)