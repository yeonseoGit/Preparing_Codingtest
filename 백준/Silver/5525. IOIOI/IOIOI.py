import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = list(input().strip())
# 2 + 1, 3 + 2, 
munja = []
for i in range(2*N+1) :
    if i % 2 == 0 :
        munja.append('I')
    else :
        munja.append('O')
cnt = 0
for j in range(M):
    if S[j] == 'I':
        if S[j:j+2*N+1] == munja :
            cnt += 1

print(cnt) 