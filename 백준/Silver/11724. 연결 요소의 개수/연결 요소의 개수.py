import sys
sys.setrecursionlimit(1000000) 
input = sys.stdin.readline

n, m = map(int, input().split())
point = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    point[a-1].append(b-1)
    point[b-1].append(a-1)
    
visit = [-1]*n

def dfs(v) :
    visit[v] = 1
    for next in point[v] :
        if visit[next] == -1 :
            dfs(next)
count = 0
for i in range(n):
    if visit[i] == -1:
        dfs(i)
        count += 1

print(count)
