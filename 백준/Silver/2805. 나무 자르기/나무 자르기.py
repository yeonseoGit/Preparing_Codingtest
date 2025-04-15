import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum((t - mid) for t in tree if t > mid)
    
    if total >= M:
        result = mid  # 조건을 만족하므로 기록하고 더 높여도 되는지 봄
        start = mid + 1
    else:
        end = mid - 1

print(result)
