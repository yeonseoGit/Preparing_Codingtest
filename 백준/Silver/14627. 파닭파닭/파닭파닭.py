import sys
input = sys.stdin.readline

s,c = map(int, input().split())
pa = []
for _ in range(s):
    pa.append(int(input()))


start = 0
end = 1000000000

result = 0
while start<=end:
    mid = (start+end)//2
    if mid==0:
        mid = 1
    cnt = 0
    for i in pa:
        cnt += i//mid
    if cnt >= c:
        result = max(result, mid)
        start = mid+1
    else:
        #더 작게 잘라야함
        end = mid-1

# 총파의양 - 치킨*결정된 파의최대길이 = 라면에넣을 파
answer = sum(pa) - (c*result)
print(answer)