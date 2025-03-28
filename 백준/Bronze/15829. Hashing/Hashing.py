n = int(input())
L = list(input())
M = 1234567891

sum_n = 0

for i in range(n):
    aa = ord(L[i]) - 96
    sum_n += aa * (31**i)
    sum_n %= M 

print(sum_n)