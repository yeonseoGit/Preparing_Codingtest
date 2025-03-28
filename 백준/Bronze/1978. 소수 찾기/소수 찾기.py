N = int(input())
Nat = list(map(int, input().split()))
cnt = 0
last = ''
for a in Nat:
    if a < 2:
        continue
    is_prime = True
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            is_prime = False
            break
    if is_prime:
        cnt += 1

print(cnt)