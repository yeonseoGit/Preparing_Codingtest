import sys
Input = sys.stdin.readline
N = int(Input())
grid = []
for i in range(N):
    grid.append(list(map(int, Input().split())))

grid = sorted(grid, key = lambda x : (x[1], x[0])) #⭐⭐⭐⭐⭐⭐

for j in range(N):
    print(*grid[j])
