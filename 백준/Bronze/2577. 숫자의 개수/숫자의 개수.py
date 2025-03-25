A = int(input())
B = int(input())
C = int(input())
r = A*B*C
anw = list(str(r))

for i in range(0, 10):
    cnt = 0 
    for j in range(0, len(anw)):
        if int(anw[j]) == i :
            cnt += 1
    print(cnt)