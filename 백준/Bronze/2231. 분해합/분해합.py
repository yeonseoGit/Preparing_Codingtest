N = int(input())
a = 0
for i in range(1, N-1):
    digit_N = sum(map(int, str(i)))
    if i+digit_N == N :
        a = i
        break
print(a)