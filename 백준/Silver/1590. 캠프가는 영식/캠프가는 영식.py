import sys
input = sys.stdin.readline

n, t = map(int, input().split())  # 버스 종류 / 도착 시간
min_wait = float('inf')

for _ in range(n):
    s, i, c = map(int, input().split())  # 시작 시각, 간격, 대수
    for k in range(c):
        bus_time = s + i * k
        if bus_time >= t:
            wait = bus_time - t
            min_wait = min(min_wait, wait)
            break  # 이 버스보다 더 늦게 오는 건 탈 필요 없음

if min_wait == float('inf'):
    print(-1)
else:
    print(min_wait)
