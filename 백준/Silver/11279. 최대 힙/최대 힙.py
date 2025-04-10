import sys
import heapq

input = sys.stdin.readline

n = int(input())
result = []
x = [int(input()) for _ in range(n)]

for i in range(0, len(x)):
    if x[i] == 0 :    
        if result:
            print(-heapq.heappop(result))
        else :
            print(0)
    else :
        heapq.heappush(result, -x[i])