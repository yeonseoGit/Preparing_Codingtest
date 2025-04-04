import sys

Input = sys.stdin.readline

T = int(Input())

if T%10 != 0 :
    print(-1)
    exit()

a = 300
b = 60
c = 10
push_a = 0
push_b = 0
push_c = 0
while T > 0 :
    if T//300 > 0 :
        push_a = T//300
        T = T%300
    elif T//60 > 0:
        push_b = T//60
        T = T%60
    else :
        push_c = T//10
        T = 0
print(push_a, push_b, push_c)