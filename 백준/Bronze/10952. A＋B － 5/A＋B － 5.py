a, b = map(int, input().split(' '))
c = []
while (a>0) and (b>0):
    c.append(a+b)
    a, b = map(int, input().split(' '))
    
for i in range(len(c)):
    print(c[i])