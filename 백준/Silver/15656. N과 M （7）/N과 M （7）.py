import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

result = []

def dfs(depth):
    if depth == m:
        print(*result)
        return
    for i in range(n):
        result.append(nums[i])
        dfs(depth + 1)
        result.pop()

dfs(0)
