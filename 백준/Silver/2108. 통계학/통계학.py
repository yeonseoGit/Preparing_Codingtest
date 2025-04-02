import sys
from collections import Counter #

Input = sys.stdin.readline

N = int(Input())
nums = [int(Input()) for _ in range(N)]

def sosu(a) :
    if a != int(a):
        if abs(a - int(a)) >= 0.5 : # 절댓값 : abs()
            if a > 0 :
                a = int(a) + 1
            else :
                a = int(a) - 1
    return int(a)


print(sosu(sum(nums)/len(nums)))

nums.sort()
print(nums[(N//2)])

ele = Counter(nums)
most_common = ele.most_common()
if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    print(most_common[1][0])  # 두 번째로 작은 값
else:
    print(most_common[0][0])  # 최빈값 하나만 있을 경우

print(nums[-1] - nums[0])