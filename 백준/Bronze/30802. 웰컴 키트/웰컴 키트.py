N = int(input())

size = list(map(int, input().split()))
T, P = map(int, input().split())
group_T = 0
group_P = []
for i in range(0, 6):
    group_T += size[i] // T
    if size[i] % T != 0:
        group_T += 1

ans2 = [int(N/P), N%P]

print(group_T)
print(*ans2)