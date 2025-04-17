import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
flat = []

for _ in range(n):
    flat.extend(map(int, input().split()))  # 2차원 → 1차원

min_time = float('inf')
result_height = 0

for target in range(257):  # 0부터 256까지 높이 모두 시도
    remove = 0
    add = 0

    for h in flat:
        if h > target:
            remove += (h - target)
        else:
            add += (target - h)

    if remove + b >= add:
        time = remove * 2 + add
        if time < min_time or (time == min_time and target > result_height):
            min_time = time
            result_height = target

print(min_time, result_height)
