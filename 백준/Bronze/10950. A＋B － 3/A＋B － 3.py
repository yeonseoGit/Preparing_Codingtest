N = int(input())
c = []
for i in range(0, N):
    a, b = map(int, input().split(' '))
    c.append(a+b)
for i in range(len(c)):
    print(c[i])