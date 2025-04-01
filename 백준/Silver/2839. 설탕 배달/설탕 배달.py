import sys

Input = sys.stdin.readline

N = int(Input())
ans = 0
while N >= 0 :
    if N % 5 == 0 :
        ans += N//5
        break
    N = N-3
    ans += 1
if N < 0 :
    ans = -1
print(ans)
