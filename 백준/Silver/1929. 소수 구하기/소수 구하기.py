import sys
import math
Input = sys.stdin.readline
M, N = map(int, Input().split())

for i in range(M, N+1):
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(math.isqrt(i)) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
