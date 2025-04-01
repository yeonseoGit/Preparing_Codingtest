import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break

    stack = []
    balanced = True

    for ch in line:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                balanced = False
                break
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balanced = False
                break

    if balanced and not stack:
        print('yes')
    else:
        print('no')
