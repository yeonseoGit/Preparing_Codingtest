import sys

input = sys.stdin.readline

T = int(input())
strr = []

for _ in range(T):
    strr.append(list(input().strip()))

cnt = 0

for word in strr:
    temp = []
    group = True
    for i in range(len(word)):
        if i > 0 and word[i] == word[i - 1]:
            continue
        if word[i] in temp:
            group = False
            break
        temp.append(word[i])
    if group:
        cnt += 1

print(cnt)