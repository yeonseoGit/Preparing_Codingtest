import sys

Input = sys.stdin.readline

N = int(Input())
cup = int(Input())
virus = [[] for _ in range(N)]
for _ in range(cup):
    a, b =  map(int, Input().split())
    virus[a-1].append(b-1)
    virus[b-1].append(a-1)

visit = [False for _ in range(N)]
def dfs(x):
    visit[x] = True
    for next in virus[x]:
        if not visit[next]:
            dfs(next)
dfs(0)  
print(visit.count(True) - 1)  