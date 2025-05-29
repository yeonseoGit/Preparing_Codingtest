import sys
input = sys.stdin.readline

n, m = map(int, input().split())
jewels = [int(input()) for _ in range(m)]

left = 1 # 받을 수 있는 보석 최소
right = max(jewels) # 받을 수 있는 보석 최대
answer = right

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for jewel in jewels:
        cnt += (jewel + mid - 1) // mid  # 올림 나눗셈

    if cnt <= n:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
