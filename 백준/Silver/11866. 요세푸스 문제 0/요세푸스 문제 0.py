import sys
Input = sys.stdin.readline

N, K = map(int, Input().split())
arr = [i for i in range(1, N+1)]
answer = []
num = 0
for _ in range(N):
    num += K-1
    if num >= len(arr):
        num = num%len(arr)
    answer.append(str(arr.pop(num)))
print("<",", ".join(answer)[:],">", sep='')