import heapq
import sys
input = sys.stdin.readline

n = int(input())  
nums = [] 
result = 0

for _ in range(n):
    heapq.heappush(nums, int(input()))  

if len(nums) == 1: 
    print(0)
else:  
    while nums:
        if len(nums) == 2:  
            print(result + sum(nums))
            break
        temp = heapq.heappop(nums) + heapq.heappop(nums) 
        heapq.heappush(nums, temp) 
        result += temp