import sys
input = sys.stdin.readline

n = int(input())

cnt = -1 

# 5원짜리를 최대한 사용하면서 2원짜리로 보완하는 방식
for i in range(n // 5, -1, -1):  # 5원짜리 동전 개수를 줄여가며 시도
    rest = n - (5 * i)
    if rest % 2 == 0:  # 남은 금액이 2원으로 나누어 떨어지면
        cnt = i + (rest // 2)
        break

print(cnt)
