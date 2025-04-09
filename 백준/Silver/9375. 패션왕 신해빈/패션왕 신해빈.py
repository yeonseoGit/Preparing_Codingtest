import sys

Input = sys.stdin.readline
T = int(Input())

# 마지막 T 번 반복문 써주기.
for _ in range(T) :
    fasion = {}
    n = int(Input())
    for _ in range(n):
        a, b = Input().strip().split()
        if b in fasion :
            fasion[b].append(a)
        else :
            fasion[b] = [a]

    result = 1
    for items in fasion.values():
        result *= (len(items) + 1)
    print(result - 1) 
