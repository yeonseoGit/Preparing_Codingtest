import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
trees_basic = list(map(int, input().split()))
remo = int(input())

tree = [[] for _ in range(n)]
root = -1

for i in range(n):
    if trees_basic[i] == -1:
        root = i
    else :
        tree[trees_basic[i]].append(i)

def dfs(node):
    if node == remo:
        return 0

    if not tree[node] or (len(tree[node]) == 1 and tree[node][0] == remo):
        return 1

    count = 0
    for child in tree[node]:
        if child != remo:
            count += dfs(child)
    return count

if root == remo:
    print(0)
else:
    print(dfs(root))