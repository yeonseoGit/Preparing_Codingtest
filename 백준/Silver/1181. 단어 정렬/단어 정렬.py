import sys
Input = sys.stdin.readline
dic = []
N = int(Input())
for _ in range(N):
    a = Input().strip()
    dic.append(a)
dic_set = set(dic)
dic = list(dic_set)

for i in range(len(dic)) :
    dic[i] = [len(dic[i]), dic[i]]
dic.sort()

for i in range(len(dic)):
    print(dic[i][1])