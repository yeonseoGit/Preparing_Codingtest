import sys
Input = sys.stdin.readline

N = int(Input())
stack = []

for _ in range(N):
    num = int(Input())
    if num != 0 :
        stack.append(num)
    else :
        stack.pop()

print(sum(stack))