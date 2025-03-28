N = int(input())
import sys
input = sys.stdin.readline

NL = [0] * 10001
for _ in range(N) :
    a = int(input())
    NL[a] += 1

for i in range(1, len(NL)):
    if NL[i] != 0 :
        for j in range(0, NL[i]) :
            print(i)
