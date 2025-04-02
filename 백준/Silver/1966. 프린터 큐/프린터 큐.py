from collections import deque
import sys

Input = sys.stdin.readline
T = int(Input())

for _ in range(T):
    N, M = map(int, Input().split())
    importance = list(map(int, Input().split()))
    queue = deque()
    # enumerate(imp) : 리스트내 인덱스(index) 와 값(value) 를 같이 꺼내주는 함수
    for i, v in enumerate(importance):
        queue.append((i, v))
    count = 0

    while queue:
        cur = queue.popleft()
        if any(cur[1] < x[1] for x in queue):
            queue.append(cur)
        else:
            count += 1
            if cur[0] == M:
                print(count)
                break
