import sys
Input = sys.stdin.readline

N, M = map(int, Input().split())

memo = [list(map(str, Input().strip().split())) for _ in range(N)]
juso_dic = {}
for i in range(len(memo)):
    juso_dic[memo[i][0]] = i
    
for _ in range(M):
    juso = Input().strip()
    num = juso_dic[juso]
    print(memo[num][1])
