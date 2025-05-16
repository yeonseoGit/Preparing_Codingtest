import sys
from collections import deque

input = sys.stdin.readline


A, B = map(int, input().split())

def bfs(a, b):
    q = deque()
    q.append((a, 1))  # (현재 숫자, 연산 횟수)

    while q:
        now, cnt = q.popleft()
        if now == b:
            return cnt
        if now * 2 <= b:
            q.append((now * 2, cnt + 1))
        if now * 10 + 1 <= b:
            q.append((now * 10 + 1, cnt + 1))
    return -1

print(bfs(A, B))
