import sys

# 미리 DP 배열 계산해두기
dp = [0] * 251
dp[0] = 1
dp[1] = 1

for i in range(2, 251):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]

# 입력을 EOF까지 받기
for line in sys.stdin:
    if line.strip() == '':
        continue  # 공백 줄 무시
    n = int(line.strip())
    print(dp[n])
