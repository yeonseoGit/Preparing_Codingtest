import sys
Input = sys.stdin.readline
N = int(Input())
for _ in range(N):
    stack = []
    stance = list(Input().strip())
    for i in range(len(stance)):
        if stance[i] == '(':
            stack.append(stance[i])
        elif stance[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else :
                stack.append(stance[i])

    if len(stack) == 0 :
        print('YES') 
    else :
        print('NO')