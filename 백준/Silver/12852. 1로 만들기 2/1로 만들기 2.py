N = int(input())
cache = [0]*(N+1)
path = [[] for _ in range(N+1)]
path[1] = [1]

for i in range(2, N+1):
    # 1을 뺐을 때
    cache[i] = cache[i-1] + 1
    path[i] = path[i-1] + [i]

    # 2로 나누었을 때
    if i % 2 == 0 and cache[i//2]+1 < cache[i]:
        cache[i] = cache[i//2]+1
        path[i] = path[i//2] + [i]

    # 3으로 나누었을 때
    if i % 3 == 0 and cache[i//3]+1 < cache[i]:
        cache[i] = cache[i//3]+1
        path[i] = path[i//3] + [i]

print(cache[N])
for i in path[N][::-1]:
    print(i, end=' ')