import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

max_s = 1
cnt = 1

maps = [list(map(int, input().strip())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        for k in range(min(n, m)):
            if i+k < n and j+k < m :
                if maps[i][j] == maps[i+k][j] == maps[i][j+k] == maps[i+k][j+k]:
                    max_s = max(max_s, (k+1)**2)
print(max_s)
