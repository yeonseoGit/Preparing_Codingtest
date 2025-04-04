from collections import deque
import sys
Input = sys.stdin.readline

n = int(Input())
dp = [[float('inf')] * (n+2) for _ in range(1001)]
q = deque([(1,0,0)])
while q:
    num,t,clip = q.popleft()
    if num == n: # 정답 도출
        print(t)
        break
        
    t+=1
    for dnum in num+clip,num-1: # 복붙, -1
        if n+2>dnum>0 and dp[clip][dnum] > t:
            dp[clip][dnum] = t
            q.append((dnum,t,clip))
    q.append((num,t,num)) # 복사