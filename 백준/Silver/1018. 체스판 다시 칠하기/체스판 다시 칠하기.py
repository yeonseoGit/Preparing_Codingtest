import sys
input = sys.stdin.readline

pan = []
N, M = map(int, input().split())
for _ in range(N):
    pan.append(list(input().strip()))

min_cnt = 2500

for k in range(N - 7):
    for l in range(M - 7):
        for first in ['W', 'B']:
            cnt = 0
            for i in range(8):
                for j in range(8):
                    expected = first if (i + j) % 2 == 0 else ('B' if first == 'W' else 'W')
                    if pan[k + i][l + j] != expected:
                        cnt += 1
            min_cnt = min(min_cnt, cnt)

print(min_cnt)