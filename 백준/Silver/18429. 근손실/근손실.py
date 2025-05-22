import sys
from itertools import permutations
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [i for i in range(n)]
# 순열 조합 생성
arr_P = list(permutations(arr))

# ep
ep = list(map(int, input().split()))
cnt = 0 

for i in range(len(arr_P)):
    weight = 500  # 초기 중량
    for j in range(n):
        weight += ep[arr_P[i][j]] - k
        if weight < 500:
            break
    else:
        cnt += 1 

print(cnt)