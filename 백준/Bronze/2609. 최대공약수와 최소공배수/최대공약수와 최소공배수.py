a, b = map(int, input().split())
max_N = 0
min_M = 1

Min_NUM = min(a, b)
for i in range(1, Min_NUM+1) : 
    if (a % i == 0) & (b % i == 0) :
        max_N  = max(i, max_N)

min_M = (a*b) //max_N
        
    
print(max_N)
print(min_M)