T = int(input())
anw = []
for _ in range(T):
    anw.append(list(str(input())))

for i in range(T):
    cnt = 0
    total = 0
    for j in anw[i]:
        if j == 'O':
            cnt += 1
            total += cnt  # O가 나올 때마다 더하기
        else:
            cnt = 0
    print(total)