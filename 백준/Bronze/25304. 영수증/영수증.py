money = int(input())
N = int(input())
c = []

for i in range(0, N):
    a, b = map(int, input().split(' '))
    c.append(a*b)

if money == sum(c):
    print('Yes')

else :
    print('No')