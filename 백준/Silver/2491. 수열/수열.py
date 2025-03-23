N = int(input())
arr = list(map(int, input().split()))

inc = 1  # 증가 수열 길이
dec = 1  # 감소 수열 길이
max_len = 1

for i in range(1, N):
    if arr[i] >= arr[i-1]:  # 증가 수열
        inc += 1
    else:
        inc = 1

    if arr[i] <= arr[i-1]:  # 감소 수열
        dec += 1
    else:
        dec = 1

    max_len = max(max_len, inc, dec)

print(max_len)
