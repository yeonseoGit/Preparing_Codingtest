import sys

Input = sys.stdin.readline
N, K = map(int, Input().split())

dongjeun = [int(Input()) for _ in range(N)]

dongjeun.reverse()
cnt = 0
for i in dongjeun :
    if i <= K :
        cnt += K//i
        K = K%i
print(cnt)