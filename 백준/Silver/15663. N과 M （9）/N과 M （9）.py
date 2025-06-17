from itertools import permutations

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
result = set()
for pers in permutations(nums, m):
    if pers not in result :
        print(*pers)
        result.add(pers)