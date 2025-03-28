N = int(input())
Max_N = 1
cnt = 1
while N > Max_N:
    Max_N += 6*cnt
    cnt += 1

print(cnt)
