import sys
input = sys.stdin.readline

print('\n'.join(map(str, sorted([int(input()) for _ in range(int(input()))]))))
