import sys
Input = sys.stdin.readline

N = int(Input())
ans = [0]*N

for i in range(0, N):
    ans[i] = int(Input())

ans.sort()

for j in range(0, N):
    print(ans[j])