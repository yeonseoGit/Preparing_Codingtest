M = list(map(int, input().split()))
M.sort()

if M[0] + M[1] > M[2]: 
    print(sum(M))
else:
    print(2 * (M[0] + M[1]) - 1)
