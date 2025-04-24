
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0] * (N+1) # parent[i]: i번 노드의 부모 노드를 저장할 리스트
visited = [False] * (N+1)

'''
dfs(node)는 현재 노드에서 연결된 자식 노드들을 재귀적으로 방문
방문 안 한 노드는 자식이므로, 그 노드의 부모를 현재 노드로 설정
재귀 호출로 자식 노드의 자식까지 모두 탐색
'''
def dfs(node):
    visited[node] = True
    for child in tree[node]:
        if not visited[child]:
            parent[child] = node
            dfs(child)

dfs(1)  # 1번 노드가 루트
# print(tree) # defaultdict(<class 'list'>, {1: [6, 4], 6: [1, 3], 3: [6, 5], 5: [3], 4: [1, 2, 7], 2: [4], 7: [4]})
for i in range(2, N+1):
    print(parent[i])
