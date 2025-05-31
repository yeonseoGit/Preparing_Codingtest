import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lec = list(map(int, input().split()))

left = max(lec)
right = sum(lec)

def count_bluray(size):
    cnt = 1  # 블루레이 개수
    total = 0
    for l in lec:
        if total + l > size:
            cnt += 1
            total = l
        else:
            total += l
    return cnt

# 이분 탐색
answer = right
while left <= right:
    mid = (left + right) // 2
    if count_bluray(mid) <= m:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
