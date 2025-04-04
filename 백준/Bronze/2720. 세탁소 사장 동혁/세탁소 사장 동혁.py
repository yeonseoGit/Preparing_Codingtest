import sys
Input = sys.stdin.readline

T = int(Input())
cnt = 0
for _ in range(T):
    cnt = [0]*4
    q = 0
    d = 0
    n = 0
    C = int(Input())
    while C > 0 :
        if C//(25) > 0 :
            q += C//25
            cnt[0] = q
            C = C%25
        elif C//(10) > 0:
            d += C//10
            cnt[1] = d
            C = C%10
        elif C//(5) > 0:
            n += C//5
            cnt[2] = n
            C = C%5
        else :
            cnt[3] = C
            break
    print(*cnt)