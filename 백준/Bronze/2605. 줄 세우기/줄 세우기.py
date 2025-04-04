import sys
Input = sys.stdin.readline

N = int(Input())
student = list(map(int, Input().split()))
ans = []
for i in range(N):
    if student[i] == 0:
        ans.insert(0, i+1)
    else :
        ans.insert(student[i], i+1)
        
for i in reversed(ans):
    print(i,end=' ')