n, k = map(int, input().split())
state = list(input())
cnt = 0

for i in range(n):
    if state[i] == 'P':
        for j in range(i - k, i + k + 1):  # i-K부터 i+K까지
            if 0 <= j < n and state[j] == 'H':
                state[j] = 'X'
                cnt += 1
                break  

print(cnt)
