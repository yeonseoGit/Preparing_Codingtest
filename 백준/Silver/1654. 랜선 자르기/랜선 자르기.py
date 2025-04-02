import sys

Input = sys.stdin.readline
K, N = map(int, Input().split())  # K <= N
init = []
for _ in range(K):
    init.append(int(Input()))

start, end = 1, max(init)
result = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for length in init:
        count += length // mid 

    if count >= N:
        result = mid 
        start = mid + 1
    else:
        end = mid - 1 

print(result)
