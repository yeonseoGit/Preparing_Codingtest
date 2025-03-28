N, M = map(int, input().split())

NL = list(map(int, input().split()))
NL.sort(reverse=True)
sum_N = 0
max_N = 0
for i in range(0, len(NL)-2) :
    for j in range(i+1, len(NL)-1):
        for k in range(j+1, len(NL)):
            sum_N = NL[i] + NL[j] + NL[k]
            if sum_N <= M :
                max_N = max(sum_N, max_N)

print(max_N)