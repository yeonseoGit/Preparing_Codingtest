import sys
input = sys.stdin.readline

# 입력받기
compute_n = int(input())
ssang = int(input())
virus = [[] for _ in range(compute_n)]

for _ in range(ssang) :
    a, b = map(int, input().split())
    virus[a-1].append(b-1)
    virus[b-1].append(a-1)

# visit 구현
visit = [False]*compute_n

cnt_d = 0

def dfs(x):
    global cnt_d
    visit[x] = True
    for i in virus[x]:
        if not visit[i]:
            cnt_d += 1
            dfs(i)

dfs(0)
print(cnt_d)