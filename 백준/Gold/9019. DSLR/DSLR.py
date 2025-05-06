# D : n을 두배로 바꿈 만약 결과값이 9999보다 크면 10000으로 나눈 나머지.
# S : n에서 1을 뺀 값 n-1 
# L : n의 자릿수를 왼편으로 회전. d2, d3, d4, d1
# R : n의 자릿수를 오른편으로 회전. d4, d1, d2, d3

# 최단 경로 탐색 문제이며, BFS (너비 우선 탐색) 를 사용하는 전형적인 문제
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs(a, b):
    visit = [False]*10000
    q = deque()
    q.append((a,"")) # 현재숫자, 명령어시퀀스
    visit[a] = True

    while q :
        now, cur = q.popleft()
        if now == b:
            return cur
        
        d = (now*2)%10000
        if not visit[d] :
            visit[d] = True
            q.append((d, cur + 'D'))
            # print(q)
        
        if now == 0 :
            s = 9999
        else :
            s = now-1
        if not visit[s]:
            visit[s] = True
            q.append((s, cur+'S'))
            # print(q)
        
        l = (now%1000)*10 + (now//1000)
        if not visit[l] :
            visit[l] = True
            q.append((l, cur+'L'))
            # print(q)
        
        r = (now%10)*1000 + (now//10)
        if not visit[r]:
            visit[r] = True
            q.append((r, cur+'R'))
            # print(q)

for _ in range(T):
    a, b = map(int, input().strip().split())
    print(bfs(a, b))