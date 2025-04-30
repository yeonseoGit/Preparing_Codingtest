import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

i = 0
count = 0
result = 0

while i < M - 1:
    if S[i] == 'I':
        temp = 0
        while i+1 < M and S[i+1] == 'O' and i+2 < M and S[i+2] == 'I':
            temp += 1
            i += 2
            if temp == N:
                result += 1
                temp -= 1  # 겹치는 패턴을 위해 하나 빼줌
        else:
            i += 1
    else:
        i += 1

print(result)
