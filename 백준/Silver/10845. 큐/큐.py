from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
q = deque()

for _ in range(N):
    order = input().strip().split()
    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if q :
            print(0)
        else :
            print(1)
    elif order[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
