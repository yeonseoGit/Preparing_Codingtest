import sys

Input = sys.stdin.readline
stack = []
gi = []
# push는 반드시 오름차순을 지킨다. 
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
#      있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지
# push연산은 +로, pop 연산은 -로 표현

n = int(Input())
ans = [int(Input()) for _ in range(n)]
cur = 1
for num in ans :
    while cur <= num :
        stack.append(cur)
        gi.append('+')
        cur += 1
    if stack[-1] == num :
        stack.pop()
        gi.append('-')
    else :
        cur = max(ans)
        break

if cur == max(ans):
    print('NO')
else :
    for i in gi :
        print(i)