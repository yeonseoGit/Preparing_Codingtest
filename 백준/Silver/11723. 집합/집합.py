import sys

Input = sys.stdin.readline

n = int(Input())
S = set() # set함수는 add, discard, remove 사용
for _ in range(n):
    sen = Input().strip().split()
    if sen[0] == 'add':
        S.add(int(sen[1]))
    elif sen[0] == 'remove':
        num = int(sen[1])
        if num in S:
            S.remove(num)
    elif sen[0] == 'check':
        if int(sen[1]) in S :
            print(1)  
        else :
            print(0)
    elif sen[0] == 'toggle':
        num = int(sen[1])
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif sen[0] == 'all':
        S = set(range(1, 21))
    elif sen[0] == 'empty':
        S.clear()
