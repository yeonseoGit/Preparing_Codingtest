S = int(input())
sum_ = 0
n = 0

for i in range(1, S + 1):
    if sum_ + i > S:
        break
    sum_ += i
    n += 1

print(n)
