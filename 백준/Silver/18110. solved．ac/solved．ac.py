import sys
import math
Input = sys.stdin.readline

N = int(Input())
aa = N*(0.15)
def sosu(a) :
    b = a - int(a)
    if b != 0 :
        if b*10 < 5 :
            c = int(a)
        else :
            c = int(a)+1
    else : 
        c = int(a)
    return c
if N != 0 :
    cc = sosu(aa)

    ans = []
    for _ in range(N):
        ans.append(int(Input()))
    ans.sort()
    result = sum(ans[cc:N-cc])/len(ans[cc:N-cc])
    print(sosu(result))
else :
    print(0)