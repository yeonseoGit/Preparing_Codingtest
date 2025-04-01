import sys

Input = sys.stdin.readline
M, N = map(int, Input().split())

# 소수 여부 저장 배열 (True로 초기화)
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False  # 0, 1은 소수가 아님

# 소수 판별
for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

# 결과 출력
for i in range(M, N + 1):
    if is_prime[i]:
        print(i)
