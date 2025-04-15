import sys
import itertools # ⭐ 조합! 여러개 뽑아서 한번 비교해봐야 할 때. 
input = sys.stdin.readline

N, M = map(int, input().split())

street = [list(map(int, input().strip().split())) for _ in range(N)]

home = []
chi = []
for i in range(N):
    for j in range(N):
        if street[i][j] == 1 :
            home.append([i,j])
        elif street[i][j] == 2:
            chi.append([i, j])

distance = [0]*len(home)
if len(chi) == M :
    for i in range(len(home)):
        min_d = N**2
        for j in range(len(chi)):
            min_d = min(min_d, abs(home[i][0] - chi[j][0]) + abs(home[i][1] - chi[j][1]))
            distance[i] = min_d
    print(sum(distance))

# 치킨집을 먼저 골라야 해. 왜냐면 치킨집에 따라 거리가 달라지니깐!
else :
    chi = list(itertools.combinations(chi, M))
    min_total = N**4 
    for j in range(len(chi)):
        total = 0
        for i in range(len(home)):
            min_d = N**2
            for k in range(M):
                min_d = min(min_d, abs(home[i][0] - chi[j][k][0]) + abs(home[i][1] - chi[j][k][1]))
            total += min_d
        min_total = min(min_total, total)

    print(min_total)