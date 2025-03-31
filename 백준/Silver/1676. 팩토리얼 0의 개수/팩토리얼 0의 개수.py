import sys

Input = sys.stdin.readline

N = int(Input())
answer = 1
for i in range(1, N+1):
    answer *= i

cnt = 0
while answer%10 == 0 :
    answer = answer//10
    cnt += 1
print(cnt)