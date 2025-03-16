N = int(input()) 
A = list(map(int, input().split()))

diff = A[0]
result = [0]

for i in range(1, N):
    diff = min(diff, A[i])
    result.append(max(result[-1], A[i] - diff)) 

print(*result)
