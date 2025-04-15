'''
X일때 걸으면 1초후 X-1, 
X일때 수간이동하면 1초후 2X

5, 10, 9, 18, 17
로직 1 : 2배했을 때, 2배보다 작으면 => 2배함. 
로직 2 : 2배했을 때, 2배보다 크면 => -1로 한번 해서 => 2배해.
로직 3 : 이전값보다 
'''
from collections import deque

N, K = map(int, input().split())
MAX = 100001
visited = [0] * MAX

queue = deque()
queue.append(N)

while queue:
    now = queue.popleft()
    
    if now == K:
        print(visited[now])
        break

    for next_pos in (now - 1, now + 1, now * 2): # now = 5니깐, 4, 6, 10 반복..!
        if 0 <= next_pos < MAX and visited[next_pos] == 0:
            visited[next_pos] = visited[now] + 1
            queue.append(next_pos)
