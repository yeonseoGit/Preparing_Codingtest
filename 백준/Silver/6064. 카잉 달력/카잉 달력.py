import sys
input = sys.stdin.readline

def solution(M, N, x, y):
    year = x
    while year <= M * N:
        if year % N == y % N:
            return year
        year += M
    return -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    years = solution(M, N, x, y)
    print(years)