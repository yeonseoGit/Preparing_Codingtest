import math

n = int(input())

if int(math.isqrt(n)) ** 2 == n:
    print(1)
    exit()

for i in range(1, int(math.isqrt(n)) + 1):
    if int(math.isqrt(n - i*i)) ** 2 == (n - i*i):
        print(2)
        exit()

for i in range(1, int(math.isqrt(n)) + 1):
    for j in range(1, int(math.isqrt(n - i*i)) + 1):
        if int(math.isqrt(n - i*i - j*j)) ** 2 == (n - i*i - j*j):
            print(3)
            exit()

print(4)
