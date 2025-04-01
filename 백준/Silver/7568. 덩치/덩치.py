import sys
Input = sys.stdin.readline

N = int(Input())
ans = [0]*N
for i in range(0, N):
    w, h = map(int, Input().split())
    ans[i] = [w, h]

result = [1]*N
for i in range(N):
    for j in range(N):
        if i != j:
            if ans[j][0] > ans[i][0] and ans[j][1] > ans[i][1]:
                result[i] += 1
print(*result)
