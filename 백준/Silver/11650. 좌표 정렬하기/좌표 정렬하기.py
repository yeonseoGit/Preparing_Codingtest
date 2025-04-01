import sys
Input = sys.stdin.readline
N = int(Input())

grid = [0]*N

for i in range(N):
    grid[i] = list(map(int, Input().split()))

grid.sort()

for j in range(N):
    print(*grid[j])