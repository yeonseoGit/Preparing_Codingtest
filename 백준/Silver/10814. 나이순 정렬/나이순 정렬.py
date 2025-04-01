import sys

Input = sys.stdin.readline

N = int(Input())
member = [0]*N

for i in range(N):
    age, name = map(str, Input().split())
    member[i] = [int(age),i, name]

member.sort()
for age, _, name in member:
    print(age, name)