import sys
input = sys.stdin.readline

N = int(input())
mp = {}
vec = []

for _ in range(N):
    s, x = input().split()
    x = int(x)
    if s in mp:
        mp[s] += x
    else:
        mp[s] = x

for value in mp.values():
    vec.append(value)

n = len(vec)
for i in range(n):
    xx = vec[i] * 1618 // 1000  # 정수 나눗셈
    for j in range(n):
        if i == j:
            continue
        if xx == vec[j]:
            print("Delicious!")
            sys.exit(0)

print("Not Delicious...")
