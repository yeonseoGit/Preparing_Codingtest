import sys
Input = sys.stdin.readline

N = int(Input())
a = 666
fin = 100000000
cnt = 0
for i in range(0, fin) :
    if str(a) in str(i) :
        cnt += 1
    if cnt == N :
        print(i)
        break