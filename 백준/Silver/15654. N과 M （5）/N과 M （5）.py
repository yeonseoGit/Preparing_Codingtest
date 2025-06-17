from itertools import permutations
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for comb in permutations(nums, m):
    comb_l = list(comb)
    print(*comb_l)