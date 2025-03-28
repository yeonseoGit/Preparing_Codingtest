n = int(input())
L = list(input())

sum_n = 0

for i in range(0, n):
    aa = ord(L[i])-96
    sum_n += aa * (31**i)

print(sum_n)
