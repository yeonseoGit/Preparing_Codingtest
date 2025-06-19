import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

target = list(map(int, input().split()))
score = [0]*n
score_p = [0]*n

games = [list(map(int, input().split())) for _ in range(m)]

for i in range(0, m):
    for j in range(0, n):
        if games[i][j] == target[i] :
            score[j] += 1
        else :
            score_p[target[i]-1] += 1

for i in range(0, n):
    print(score[i]+score_p[i])