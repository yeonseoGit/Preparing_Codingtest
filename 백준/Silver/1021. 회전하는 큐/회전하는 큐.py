import sys
from collections import deque
Input = sys.stdin.readline

N, M = map(int, Input().split())
queue = deque(range(1, N + 1))
nums = list(map(int, Input().split()))
cnt = 0

for j in nums:
    idx = queue.index(j)
    if idx == 0:
        queue.popleft()
    else:
        if idx <= len(queue) // 2:
            while queue[0] != j:
                queue.append(queue.popleft())
                cnt += 1
        else:
            while queue[0] != j:
                queue.appendleft(queue.pop())
                cnt += 1
        queue.popleft()

print(cnt)
