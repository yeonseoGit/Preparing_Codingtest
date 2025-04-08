import sys
Input = sys.stdin.readline

N, M = map(int, Input().split())

no_listening = set(Input().strip() for _ in range(N))  # 리스트 → 집합
result = []

for _ in range(M):
    x = Input().strip()
    if x in no_listening:
        result.append(x)

result.sort()  # 사전순 정렬 필요할 수 있음 (문제 조건에 따라)

print(len(result))
for name in result:
    print(name)