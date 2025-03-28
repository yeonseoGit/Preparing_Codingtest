import sys
Input = sys.stdin.readline().strip()

N,K = map(int, Input.split()) # 5 2

nn = 1
kk = 1
for i in range(1, K+1): # 1 2
    nn *= N # 5, 
    N -= 1
for j in range(2, K+1):
    kk *= j

print(nn//kk)