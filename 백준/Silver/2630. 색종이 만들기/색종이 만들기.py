import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

cnt_w = 0
cnt_b = 0

def divide(x, y, size):
    global cnt_w, cnt_b
    color = paper[x][y]
    all_same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                all_same = False
                break
        if not all_same:
            break

    if all_same:
        if color == 0:
            cnt_w += 1
        else:
            cnt_b += 1
    else:
        half = size // 2
        divide(x, y, half)    
        divide(x, y + half, half) 
        divide(x + half, y, half) 
        divide(x + half, y + half, half) 

divide(0, 0, n)

print(cnt_w)
print(cnt_b)