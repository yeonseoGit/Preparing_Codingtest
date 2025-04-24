import sys 
input = sys.stdin.readline

n, m = map(int, input().split())

tree = []

min_t = n-m

for i in range(0, min_t) :
    tree.append([i, i+1])

leaf_start = min_t+1
for i in range(m-1):
    tree.append([min_t, leaf_start + i])

for i in range(len(tree)):
    print(*tree[i])