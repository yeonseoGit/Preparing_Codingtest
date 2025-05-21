import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())

arr_a = [[0]*w for _ in range(h)]
arr_b = [list(map(int, input().split())) for _ in range(h+x)]

for i in range(h):
    for j in range(w):
        # 겹치는 부분이면 이전 arr_a에서 빼주기
        if i >= x and j >= y:
            arr_a[i][j] = arr_b[i][j] - arr_a[i - x][j - y]
        else:
            arr_a[i][j] = arr_b[i][j]

for row in arr_a:
    print(*row)
