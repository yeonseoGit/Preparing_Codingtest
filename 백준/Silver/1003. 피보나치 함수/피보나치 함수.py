# 0과 1의 호출 횟수를 저장하는 배열
dp = [(0, 0)] * 41  # 최대 n이 40이므로, 41개의 값을 미리 저장

def fibonacci(n):
    # 이미 계산된 경우 바로 반환
    if dp[n] != (0, 0):
        return dp[n]
    
    if n == 0:
        dp[n] = (1, 0)  # 0이 1번 호출, 1이 0번 호출
    elif n == 1:
        dp[n] = (0, 1)  # 0이 0번 호출, 1이 1번 호출
    else:
        fib_n1 = fibonacci(n - 1)
        fib_n2 = fibonacci(n - 2)
        dp[n] = (fib_n1[0] + fib_n2[0], fib_n1[1] + fib_n2[1])  # 0과 1 호출 횟수 합산
    
    return dp[n]

# 입력 처리
t = int(input())  # 테스트 케이스 수
for _ in range(t):
    n = int(input())
    result = fibonacci(n)
    print(result[0], result[1])

    
'''
zero_count = 0
one_count = 0

def fibonacci(n):
    global zero_count, one_count
    
    if n == 0:
        zero_count += 1
        return 0
    elif n == 1:
        one_count += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 입력 처리
t = int(input())  # 테스트 케이스 수
for _ in range(t):
    zero_count = 0
    one_count = 0
    n = int(input())
    fibonacci(n)
    print(zero_count, one_count)

'''