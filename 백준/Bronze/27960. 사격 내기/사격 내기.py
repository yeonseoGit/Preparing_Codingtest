import sys
from itertools import combinations

input = sys.stdin.readline

lst = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

a, b = map(int, input().split())

if a == b:
    print(0)
    exit()

a_list = []
for r in range(1, len(lst) + 1):
    for comb in combinations(lst, r):
        if sum(comb) == a:
            a_list = list(comb)
            break
    if a_list:
        break

b_list = []
for r in range(1, len(lst) + 1):
    for comb in combinations(lst, r):
        if sum(comb) == b:
            b_list = list(comb)
            break
    if b_list:
        break

# 이제 a_list 와 b_list 비교
result_c = []

for bullet in a_list:
    if bullet not in b_list:
        result_c.append(bullet)

for bullet in b_list:
    if bullet not in a_list:
        result_c.append(bullet)

print(sum(result_c))
